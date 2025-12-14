from django.contrib import admin

from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
	list_display = ('reference', 'amount', 'currency', 'method', 'status', 'created_at')
	search_fields = ('reference', 'donor_email', 'donor_name')
	list_filter = ('method', 'status', 'currency')
