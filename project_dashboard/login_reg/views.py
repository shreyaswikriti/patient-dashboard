from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
import logging
from .utility import *

logger = logging.getLogger(__name__)

# Create your views here.
# @login_required(login_url='reg_doc')
def home(request):
	logger.info("Registration/login page requested")
	return render(request, 'registration_login.html', {})

# def register_user(request):
#     if request.method=="POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             login(request,user)
#             messages.success(request,('You have registered....'))
#             return redirect('register_user')
#     else:
#             form=RegisterForm()
#     context = {'form':form}
#     return render(request, 'registration_login.html', context)

def register_doc(request):
	if request.method=='POST':
		form = UserAdminCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			logger.info("User is Created")
			user = authenticate(request, username=username, password=password)
			login(request, user)
			logger.info("User has been loggen in")
			messages.success(request,('You have registered....'))
			return redirect('home')
	else:
		form = UserAdminCreationForm()
	context = {'form' : form}
	return render(request, 'doc_reg.html', context)

def register_hospital(request):
	if request.method=='POST':
		form = UserAdminCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			logger.info("User is Created")
			user = authenticate(request, username=username, password=password)
			login(request, user)
			logger.info("User has been loggen in")
			messages.success(request,('You have registered....'))
			return redirect('home')
	else:
		form = UserAdminCreationForm()
	context = {'form' : form}
	return render(request, 'hospital_reg.html', context)


def register_patient(request):
	if request.method=='POST':
		form = UserAdminCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			logger.info("User is Created")
			user = authenticate(request, username=username, password=password)
			login(request, user)
			logger.info("User has been loggen in")
			messages.success(request,('You have registered....'))
			return redirect('home')
	else:
		form = UserAdminCreationForm()
	context = {'form' : form}
	return render(request, 'patient_reg.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, ('You have logged out'))
    return redirect('home')



def login_user(request):
    if request.method =='POST':
        username = request.POST['email']
        password = request.POST['password']
        users = authenticate(request,username=username,password=password)
        if users is not None:
            login(request, users)
            messages.success(request, ('You have logged In!'))
            return redirect('home')
        else:
            messages.success(request, ('Error Logging-In, Please Try Again...'))
            return redirect('home')

    else:
        return render(request,'registration_login.html',{})

