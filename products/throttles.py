from rest_framework.throttling import UserRateThrottle

class PricingRateThrottle(UserRateThrottle):
    scope = 'pricing'