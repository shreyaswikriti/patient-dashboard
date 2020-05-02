from django.shortcuts import render
from login_reg.decorators import allowed_roles
from .models import DoctorProfile, DoctorEducation
# Create your views here.
import logging

logger = logging.getLogger(__name__)


# @allowed_roles(allowed_roles=['DOCTOR'])
def doc_dash(request):
	# detail = DoctorProfile.objects.filter(user=request.user).first()
	# education = DoctorEducation.objects.filter(doctor=detail.id)
	# logger.info("Doctor firstName "+detail.firstName)
	return render(request, 'doctor_dashboard.html', {})



# @allowed_roles(allowed_roles=['DOCTOR'])
def doctor_profile(request):

	return render(request, 'doctor_profile.html', {})