from django.shortcuts import redirect
from django.urls import reverse

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user is authenticated and if not, redirect to login page
        if not request.user.is_authenticated:
            return redirect(reverse('client_login'))  # Assuming your login URL name is 'login'

        response = self.get_response(request)
        return response
