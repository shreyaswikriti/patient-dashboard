from django.shortcuts import render, redirect
from login_reg.decorators import allowed_roles
from .models import PatientProfile, PatientTreatment, TreatmentComment
from doctor.models import DoctorSpecialisation
from django.contrib.auth.decorators import login_required

# Create your views here.
import logging

logger = logging.getLogger(__name__)

@login_required
@allowed_roles(allowed_roles=['PATIENT'])
def treatment_list(request):
	# logger.info("Requesting for registration or Login Page")
	patient = PatientProfile.objects.filter(user=request.user).first()
	if patient is None:
		logger.error("Patient not found")
		redirect('error')
	treatments = PatientTreatment.objects.filter(patient=patient).order_by('last_edited')
	if treatments is None:
		logger.info("Patient was never diagnised")
	context = {'treatments': treatments, 'patient':patient}
	return render(request, 'patient_dashboard.html', context)



def patient_profile(request):
	return render(request, 'patient_profile.html', {})


@login_required
@allowed_roles(allowed_roles=['PATIENT'])
def patient_detail(request, pk):
	treatment = PatientTreatment.objects.filter(id=pk).first()
	if treatment is None:
		logger.error("Treatment does not exist")
		redirect('error')
	comments = TreatmentComment.objects.filter(treatment=treatment).order_by('timestamp')
	if comments is None:
		logger.info("No comments available")
	context = {'comments':comments, 'treatment':treatment}
	return render(request, 'patient_detail.html', context)


@login_required
def doctor_search(request):
	query = request.GET['query']
	rs = DoctorSpecialisation.objects.filter(treatment__icontains=query)
	context = {'rs':rs}
	return render(request, 'doctor_search.html', context)

@login_required
def make_appointment(request):
	doc = request.POST['doctor']
	logger.info("Doctor with id {} got request for appointment".format(doc))
	context = {}
	return render(request, 'appointment.html', context)
