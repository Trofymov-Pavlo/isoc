from rest_framework import viewsets, status
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
