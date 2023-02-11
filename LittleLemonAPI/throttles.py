from rest_framework.throttling import UserRateThrottle

class TenCallesPerMinute(UserRateThrottle):
    scope = 'ten'