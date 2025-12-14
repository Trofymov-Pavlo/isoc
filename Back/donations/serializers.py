from rest_framework import serializers
from .models import Donation


class DonationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Donation
    fields = [
        'id', 'reference', 'donor_name', 'donor_email', 'amount', 'currency',
        'method', 'message', 'status', 'created_at'
    ]
    read_only_fields = ['id', 'reference', 'status', 'created_at']

  def validate_amount(self, value):
    if value <= 0:
      raise serializers.ValidationError('Le montant doit être supérieur à 0.')
    return value
