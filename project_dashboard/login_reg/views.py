from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
	logger.info("Requesting for registration or Login Page")
	return render(request, 'registration_login.html', {})

# def login(request):
# 	username = request.POST['username']
#     password = request.POST['password']
#     try:
#     	user = authenticate(request, username=username, password=password)
#     	logger.info("Checking for the authentication")
#    	except:
#    		logger.error("User in None")
#     if user is not None:
#         login(request, user)
#         logger.info("User has been logged in")
#         return render(request, 'patient' )
#     else:


# def logout_view(request):
# 	try:
#     	logout(request)
#     	logger.info("User has been logged out")
#     except:
#     	logger.error("User was not able to logout")
#     return render(request, 'registration_login.html', {})