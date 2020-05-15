from django.shortcuts import render, redirect
from login_reg.decorators import allowed_roles
from .models import DoctorProfile, DoctorEducation
from patient.models import PatientTreatment, PatientAppointment, TreatmentComment
from .models import DoctorProfile, DoctorEducation, DoctorSpecialisation
from patient.models import PatientTreatment, PatientAppointment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
import logging

logger = logging.getLogger(__name__)

@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def doc_dash(request):
	doctor = DoctorProfile.objects.filter(user=request.user).first()
	if doctor is None:
		logger.error("There is no doctor")
		redirect('error')
	patients = PatientTreatment.objects.filter(doctor=doctor).order_by('last_edited')
	if patients is None:
		logger.info("No patient is here treated by this doctor")
	appointments = PatientAppointment.objects.filter(doctor=doctor,status='REQUESTED').order_by('timestamp')[:6]
	count = PatientAppointment.objects.filter(doctor=doctor,status='REQUESTED').count();
	context = {"patients": patients, 'appointments':appointments, 'count':count}
	return render(request, 'doctor_dashboard.html', context)



# @allowed_roles(allowed_roles=['DOCTOR'])
def doctor_profile(request):
	try:
		prof = DoctorProfile.objects.filter(user=request.user).first()
		logger.info("Name:{}{} Dob:{} Gender:{} Hospital:{}".format(prof.firstName,prof.lastName,prof.dob,prof.gender,prof.hospital))

		educ = DoctorEducation.objects.filter(doctor=prof).first()
		logger.info("College:{} Degree:{}".format(educ.college,educ.degree))

		spec = DoctorSpecialisation.objects.filter(doctor=prof).first()
		logger.info("Treatment:{}".format(spec.treatment))

	except:
		logger.error("Not found")


	return render(request, 'doctor_profile.html', {"prof":prof,"educ":educ,"spec":spec})


@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def edit_profile(request):
	logger.info('')
	if request.method=='POST':
		try:
			firstName = request.POST['firstName']
			lastName = request.POST['lastName']
			dob = request.POST['dob']
			gender = request.POST['gender']
			hospital = request.POST['hospital']
			
		except:
			logger.error("None")
		DoctorProfile.objects.filter(user=request.user).update(
			firstName=firstName,
			lastName=lastName,
			dob=dob,
			gender=gender,
			hospital=hospital,
			user=request.user)
		profile = DoctorProfile.objects.filter(user=request.user).first()
		DoctorEducation.objects.filter(doctor=profile).update(
			college=college,
			degree=degree,
			user=request.user)
		DoctorSpecialisation.objects.filter(doctor=profile).update(
			treatment=treatment,
			user=request.user)
		logger.info("Profile edited")
		messages.success(request,("Your profile has be edited"))
		return redirect('doctor_profile')
	else:
		# Edit = edit_profile.objects.filter(id=pk).first()
		prof = DoctorProfile.objects.filter(user=request.user).first()
		return render(request,'edit_profile.html',{'prof':prof})


@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def requested_appointment(request):
	doctor = DoctorProfile.objects.filter(user=request.user).first()
	appointments = PatientAppointment.objects.filter(doctor=doctor,status='REQUESTED').order_by('timestamp')
	context = {'appointments':appointments}
	return render(request, 'requested_appointment.html', context)


@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def update_appointment(request):
	try:
		status = request.GET['status'].upper()
		appointment_id = request.GET['appointment_id']
		logger.info("Status: {} Appointment Id: {}".format(status, appointment_id))
	except:
		logger.info("Invalide submition")
		messages.error("Appointment updation failed")
		redirect('home')
	PatientAppointment.objects.filter(id=appointment_id).update(status=status)
	messages.success(request, "You have successfully updated the appointments")
	context ={}
	return redirect('home')


@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def all_appointment(request):
	doctor = DoctorProfile.objects.filter(user=request.user).first()
	appointments = PatientAppointment.objects.filter(doctor=doctor)
	context = {'appointments': appointments}
	return render(request, 'all_appointment.html', context)


@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def confirmed_appointment(request):
	doctor = DoctorProfile.objects.filter(user=request.user).first()
	appointments = PatientAppointment.objects.filter(doctor=doctor, status="CONFIRMED")
	context = {'appointments': appointments}
	return render(request, 'confirmed_appointment.html', context)







@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def patient_treatment(request, pk):
	doctor = DoctorProfile.objects.filter(user=request.user).first()
	treatmentd = PatientTreatment.objects.filter(id=pk).first()
	treatments = PatientTreatment.objects.filter(patient=treatmentd.patient)
	context = {'treatments':treatments, 'treatmentd':treatmentd}
	return render(request, 'patient_treatment.html', context)



@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def treatment_detail(request, pk):
	treatment = PatientTreatment.objects.filter(id=pk).first()
	if treatment is None:
		logger.error("Treatment does not exist")
		redirect('error')
	comments = TreatmentComment.objects.filter(treatment=treatment).order_by('timestamp')
	if comments is None:
		logger.info("No comments available")
	context = {'comments':comments, 'treatment':treatment}
	return render(request, 'treatment_detail.html', context)
