from django.shortcuts import render, redirect
from login_reg.decorators import allowed_roles
from .models import DoctorProfile, DoctorEducation
from patient.models import PatientTreatment
# Create your views here.
import logging

logger = logging.getLogger(__name__)


@allowed_roles(allowed_roles=['DOCTOR'])
def doc_dash(request):
	doctor = DoctorProfile.objects.filter(user=request.user).first()
	if doctor is None:
		logger.error("There is no doctor")
		redirect('error')
	patients = PatientTreatment.objects.filter(doctor=doctor).order_by('last_edited')
	if patients is None:
		logger.info("No patient is here treated by this doctor")

	context = {"patients": patients}
	return render(request, 'doctor_dashboard.html', context)



# @allowed_roles(allowed_roles=['DOCTOR'])
def doctor_profile(request):

	return render(request, 'doctor_profile.html', {})