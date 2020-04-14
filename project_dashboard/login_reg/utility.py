from django.contrib.auth import authenticate, login , logout, update_session_auth_hash
from .forms import *
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def register_user(request):
	form = RegisterForm(request.POST)
	if form.is_valid():
		form.save()
		username = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = authenticate(request, username=username, password=password)
		login(request,user)
		messages.success(request,('You have registered....'))