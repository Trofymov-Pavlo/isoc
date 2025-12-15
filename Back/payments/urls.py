from django.urls import path
from . import views

urlpatterns = [
    path("paypal/create/", views.paypal_create_order, name="paypal_create_order"),
    path("paypal/capture/", views.paypal_capture_order, name="paypal_capture_order"),
]
