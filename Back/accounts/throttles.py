from rest_framework.throttling import AnonRateThrottle


class SignupRateThrottle(AnonRateThrottle):
    """Limit signup to 5 per hour per IP"""
    rate = '5/hour'
    scope = 'signup'


class LoginRateThrottle(AnonRateThrottle):
    """Limit login to 10 per minute per IP"""
    rate = '10/min'
    scope = 'login'


class PasswordResetRateThrottle(AnonRateThrottle):
    """Limit password reset to 3 per hour per IP"""
    rate = '3/hour'
    scope = 'password_reset'
