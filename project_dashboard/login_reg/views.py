from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
import logging
from .utility import *
from .models import *
from django.db import transaction
from .decorators import unathenticated_user


logger = logging.getLogger(__name__)

# Create your views here.
# @login_required(login_url='reg_doc')
def home(request):
	logger.info("Registration/login page requested")
	if request.user.is_authenticated:
		try:
			roles = UserRoles.objects.filter(user=request.user).first().roles
			if roles is not None:
				if roles == 'DOCTOR':
					return redirect('doc_dash')
				elif roles == "PATIENT":
					return redirect('patient_detail')
				elif roles == "HOSPITAL":
					return redirect('hosp_dash')
			else:
				logger.error("User role is none")
				messages.error("User has no role")
				return redirect("error")
		except:
			logger.error("User has no roles")
	else:
		return render(request, 'registration_login.html', {})


def error(request):
	return render(request, 'error.html', {})

@unathenticated_user
@transaction.atomic
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
			logger.info("Users role has been assigned")
			UserRoles.objects.create(user=request.user, roles="DOCTOR")
			logger.info("User has been loggen in")
			messages.success(request,('You have registered....'))
			return redirect('home')
	else:
		form = UserAdminCreationForm()
	context = {'form' : form}
	return render(request, 'doc_reg.html', context)

@unathenticated_user
@transaction.atomic
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
			UserRoles.objects.create(user=request.user, roles="HOSPITAL")
			logger.info("User has been loggen in")
			messages.success(request,('You have registered....'))
			return redirect('home')
	else:
		form = UserAdminCreationForm()
	context = {'form' : form}
	return render(request, 'hospital_reg.html', context)

@unathenticated_user
@transaction.atomic
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
			UserRoles.objects.create(user=request.user, roles="PATIENT")
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


@unathenticated_user
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

