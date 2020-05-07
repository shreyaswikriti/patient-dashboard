from django.shortcuts import render, redirect

from login_reg.decorators import allowed_roles
from doctor.models import DoctorProfile
from .models import hospitalProfile, hospitalAddress
# Create your views here.

@allowed_roles(allowed_roles=['HOSPITAL'])
def hosp_dash(request):
	hospital = hospitalProfile.objects.filter(user=request.user).first()
	if hospital is None:
		logger.error("There is no hospital")
		redirect('error')
	doctors = DoctorProfile.objects.filter(hospital=hospital).order_by('timestamp')
	if doctors is None:
		logger.info("There is no Doctor")
	context  = {'doctors':doctors}
	return render(request, 'hospital_dashboard.html', context)


@allowed_roles(allowed_roles=['HOSPITAL'])
def hospital_profile(request):
	return render(request, 'hospital_profile.html', {})