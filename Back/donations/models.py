from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string


def generate_reference() -> str:
	# Short unique reference used by the donation flow.
	return get_random_string(12).upper()


class Donation(models.Model):
	METHOD_CHOICES = [
			('card', 'Carte bancaire'),
			('paypal', 'PayPal'),
	]

	STATUS_CHOICES = [
			('initiated', 'Initiée'),
			('authorized', 'Autorisée'),
			('failed', 'Échouée'),
	]

	user = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.SET_NULL,
			null=True,
			blank=True,
			related_name='donations'
	)
	donor_name = models.CharField(max_length=120, blank=True)
	donor_email = models.EmailField(blank=True)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	currency = models.CharField(max_length=3, default='EUR')
	method = models.CharField(max_length=20, choices=METHOD_CHOICES)
	message = models.TextField(blank=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='initiated')
	reference = models.CharField(max_length=24, default=generate_reference, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self) -> str:
		return f"{self.reference} - {self.amount} {self.currency} ({self.method})"

# Create your models here.
