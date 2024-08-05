from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Call the parent authenticate method to perform token validation
        user, token = super().authenticate(request)
        
        if user is None:
            # Allow the request to pass through without authentication
            return None
        
        return user, token