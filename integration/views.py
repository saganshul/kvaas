from django.shortcuts import render
from firebase_token_generator import create_token
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
# Create your views here.
def generate_firebase_token(request):
    if request.user.is_authenticated():
        auth_payload = { "uid": str(request.user.id), "fullname": request.user.first_name, "email": request.user.email }
        token = create_token(settings.FIRECHAT_SECURITY_TOKEN, auth_payload)
        return HttpResponse(token)
    else:
        return HttpResponse("You need to login first.")
