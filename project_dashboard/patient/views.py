from django.shortcuts import render
from login_reg.decorators import allowed_roles

# Create your views here.
import logging

logger = logging.getLogger(__name__)


# @allowed_roles(allowed_roles=['PATIENT', 'HOSPITAL', 'DOCTOR'])
def patient_detail(request):
	# logger.info("Requesting for registration or Login Page")
	return render(request, 'patient_dashboard.html', {})

def patient_profile(request):
	return render(request, 'patient_profile.html', {})