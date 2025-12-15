from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment, LiveEnvironment
from django.conf import settings


def get_paypal_client() -> PayPalHttpClient:
    """Return configured PayPal HTTP client based on environment."""
    if settings.PAYPAL_ENV == "live":
        env = LiveEnvironment(settings.PAYPAL_CLIENT_ID, settings.PAYPAL_CLIENT_SECRET)
    else:
        env = SandboxEnvironment(settings.PAYPAL_CLIENT_ID, settings.PAYPAL_CLIENT_SECRET)
    return PayPalHttpClient(env)
