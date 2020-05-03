from django.shortcuts import render
from login_reg.decorators import allowed_roles



from .models import PatientProfile,PatientAddress,PatientTreatment

# Create your views here.
import logging

logger = logging.getLogger(__name__)


# @allowed_roles(allowed_roles=['PATIENT', 'HOSPITAL', 'DOCTOR'])
def patient_detail(request):
	# logger.info("Requesting for registration or Login Page")
	return render(request, 'patient_dashboard.html', {})


def patient_profile(request):
	try:
		detail=PatientProfile.objects.filter(user=request.user).first()
		logger.info("Name:{} {} dob: {} and Gender: {}".format(detail.firstName, detail.lastName, detail.dob, detail.gender))
		details=PatientAddress.objects.filter(user=request.user).first()
		logger.info("Address:{} city:{} District: {} Locality: {} State: {} Pincode: {} Nationality: {} contactno:{}".format(details.Address, details.city, details.district, details.locality,details.state,details.pincode,details.nationality,details.contactno))
		T=PatientTreatment.objects.filter(patient__user=request.user).first()
		logger.info("Diagnosis:{} Prescription: {} ".format(T.diagnosis, T.prescription))
	except:
		logger.error("oject not found")
	return render(request, 'patient_profile.html', {"detail":detail,"details":details,"T":T}) 
	
