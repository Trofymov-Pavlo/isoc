from decimal import Decimal
import requests
import stripe
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .models import Donation
from .serializers import DonationSerializer


class DonationViewSet(viewsets.ModelViewSet):
	queryset = Donation.objects.all()
	serializer_class = DonationSerializer

	def get_permissions(self):
		# Creation ouverte, consultation réservée à l'admin pour éviter d'exposer les données donateurs.
		if self.action in ['create']:
			return [AllowAny()]
		return [IsAdminUser()]

	def perform_create(self, serializer):
		user = self.request.user if self.request.user.is_authenticated else None
		serializer.save(user=user, status='initiated')

	def create(self, request, *args, **kwargs):
		response = super().create(request, *args, **kwargs)
		# Retourne une indication de prochaine étape paiement (simulation / à brancher sur PSP réel).
		data = response.data
		data['payment_instructions'] = (
			"Paiement en attente. Rediriger le donateur vers le prestataire carte ou PayPal, "
			"puis confirmer via l'API lorsque l'autorisation est reçue."
		)
		return Response(data, status=status.HTTP_201_CREATED)

	@action(detail=True, methods=['post'], permission_classes=[AllowAny], url_path='checkout/card')
	def checkout_card(self, request, pk=None):
		donation = self.get_object()
		if not settings.STRIPE_SECRET_KEY:
			return Response({'error': 'Stripe n\'est pas configuré (STRIPE_SECRET_KEY manquant).'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

		stripe.api_key = settings.STRIPE_SECRET_KEY
		success_url = settings.DONATION_SUCCESS_URL.format(reference=donation.reference)
		cancel_url = settings.DONATION_CANCEL_URL.format(reference=donation.reference)

		try:
			amount_cents = int(Decimal(donation.amount) * 100)
			session = stripe.checkout.Session.create(
				mode='payment',
				payment_method_types=['card'],
				line_items=[{
					'price_data': {
						'currency': donation.currency.lower(),
						'product_data': {'name': f"Don {donation.reference}"},
						'unit_amount': amount_cents,
					},
					'quantity': 1,
				}],
				metadata={'donation_id': donation.id, 'reference': donation.reference},
				customer_email=donation.donor_email or None,
				success_url=success_url,
				cancel_url=cancel_url,
			)
			return Response({'checkout_url': session.url, 'reference': donation.reference}, status=status.HTTP_200_OK)
		except Exception as exc:  # StripeError captured as generic to avoid leaking details
			return Response({'error': str(exc)}, status=status.HTTP_502_BAD_GATEWAY)

	@action(detail=True, methods=['post'], permission_classes=[AllowAny], url_path='checkout/paypal')
	def checkout_paypal(self, request, pk=None):
		donation = self.get_object()
		if not settings.PAYPAL_CLIENT_ID or not settings.PAYPAL_CLIENT_SECRET:
			return Response({'error': 'PayPal n\'est pas configuré (client_id / secret manquants).'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

		base_url = settings.PAYPAL_API_BASE.rstrip('/')
		success_url = settings.DONATION_SUCCESS_URL.format(reference=donation.reference)
		cancel_url = settings.DONATION_CANCEL_URL.format(reference=donation.reference)

		try:
			token_resp = requests.post(
				f"{base_url}/v1/oauth2/token",
				data={'grant_type': 'client_credentials'},
				auth=(settings.PAYPAL_CLIENT_ID, settings.PAYPAL_CLIENT_SECRET),
				timeout=10,
			)
			token_resp.raise_for_status()
			access_token = token_resp.json().get('access_token')
			if not access_token:
				return Response({'error': 'Impossible d\'obtenir un token PayPal.'}, status=status.HTTP_502_BAD_GATEWAY)

			order_body = {
				'intent': 'CAPTURE',
				'purchase_units': [{
					'amount': {
						'currency_code': donation.currency.upper(),
						'value': str(donation.amount),
					},
					'description': f"Don {donation.reference}",
				}],
				'application_context': {
					'return_url': success_url,
					'cancel_url': cancel_url,
				},
			}

			order_resp = requests.post(
				f"{base_url}/v2/checkout/orders",
				headers={
					'Authorization': f'Bearer {access_token}',
					'Content-Type': 'application/json',
				},
				json=order_body,
				timeout=10,
			)
			order_resp.raise_for_status()
			order_data = order_resp.json()
			approval_url = next((link.get('href') for link in order_data.get('links', []) if link.get('rel') == 'approve'), None)
			if not approval_url:
				return Response({'error': 'Lien d\'approbation PayPal introuvable.'}, status=status.HTTP_502_BAD_GATEWAY)

			return Response({'approval_url': approval_url, 'reference': donation.reference}, status=status.HTTP_200_OK)
		except requests.RequestException as exc:
			return Response({'error': str(exc)}, status=status.HTTP_502_BAD_GATEWAY)
