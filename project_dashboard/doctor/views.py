from django.shortcuts import render, redirect
from login_reg.decorators import allowed_roles
from .models import DoctorProfile, DoctorEducation
from patient.models import PatientTreatment, PatientAppointment, TreatmentComment, PatientProfile, PatientAddress
from .models import DoctorProfile, DoctorEducation, DoctorSpecialisation
from patient.models import PatientTreatment, PatientAppointment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utility import get_treatment_details, edit_treatment_detail
from django.http import HttpResponseRedirect
from django.urls import reverse
from hospital.models import hospitalProfile
# Create your views here.
import logging

logger = logging.getLogger(__name__)

@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def doc_dash(request):
	doctor = DoctorProfile.objects.filter(user=request.user).first()
	if doctor is None:
		logger.error("There is no doctor")
		return redirect('error')
	patients = PatientTreatment.objects.filter(doctor=doctor).order_by('last_edited')
	if patients is None:
		logger.info("No patient is here treated by this doctor")
	appointments = PatientAppointment.objects.filter(doctor=doctor,status='REQUESTED').order_by('timestamp')[:6]
	count = PatientAppointment.objects.filter(doctor=doctor,status='REQUESTED').count();
	context = {"patients": patients, 'appointments':appointments, 'count':count, 'doctor':doctor}
	return render(request, 'doctor_dashboard.html', context)



# @allowed_roles(allowed_roles=['DOCTOR'])
def doctor_profile(request):
	try:
		prof = DoctorProfile.objects.filter(user=request.user).first()
		logger.info("Name:{}{} Dob:{} Gender:{} Hospital:{}".format(prof.firstName,prof.lastName,prof.dob,prof.gender,prof.hospital))

		educs = DoctorEducation.objects.filter(doctor=prof)

		specs = DoctorSpecialisation.objects.filter(doctor=prof)

	except:
		logger.error("Not found")


	return render(request, 'doctor_profile.html', {"prof":prof,"educs":educs,"specs":specs})


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
		hospital = hospitalProfile.objects.all()
		context = {'prof': prof, 'hospital':hospital}
		return render(request,'edit_profile.html', context)


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
		return redirect('home')
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
	treatments = PatientTreatment.objects.filter(patient=treatmentd.patient, parent_treatment__isnull=True)
	context = {'treatments':treatments, 'treatmentd':treatmentd}
	return render(request, 'patient_treatment.html', context)



@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def treatment_detail(request, pk):
	if request.method=='POST':
		treatment = PatientTreatment.objects.filter(id=pk).first()
		doctor = DoctorProfile.objects.filter(user=request.user).first()
		comments = request.POST['comment']
		TreatmentComment.objects.create(comment=comments, treatment=treatment, doctor=doctor)
		context = get_treatment_details(request, pk)
		return render(request, 'treatment_detail.html', context)
	else:
		context = get_treatment_details(request, pk)
		return render(request, 'treatment_detail.html', context)




@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def edit_treatment(request):
	if request.method=='POST':
		diagnosis = request.POST['diagnosis']
		prescription = request.POST['prescription']
		treatment_id = request.POST['treatment_id']
		doctor = DoctorProfile.objects.filter(user=request.user).first()
		patient = PatientTreatment.objects.filter(id=treatment_id).first().patient
		count = PatientTreatment.objects.filter(parent_treatment=treatment_id).order_by('-count').first()
		if count is None:
			edit_treatment_detail(request, count=1,
				diagnosis=diagnosis, prescription=prescription, treatment_id=treatment_id,
				patient=patient, doctor=doctor)
		else:
			logger.info("I am printing or not")
			edit_treatment_detail(request, count=(count.count+1),
				diagnosis=diagnosis, prescription=prescription, treatment_id=treatment_id,
				patient=patient, doctor=doctor)
		context = get_treatment_details(request, treatment_id)
		return HttpResponseRedirect(reverse('treatment_detail', args=(treatment_id,)))




@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def add_treatment(request, pk):
	if request.method=='POST':
		diagnosis = request.POST['diagnosis']
		prescription =request.POST['prescription']
		PatientAppointment.objects.filter(id=pk).update(status='DONE')
		appointment = PatientAppointment.objects.filter(id=pk).first()
		PatientTreatment.objects.create(doctor=appointment.doctor, patient=appointment.user,
			diagnosis=diagnosis, prescription=prescription, active=True)
		treatment_id = PatientTreatment.objects.filter(doctor=appointment.doctor, patient=appointment.user, active=True).first().id
		return HttpResponseRedirect(reverse('treatment_detail', args=(treatment_id,)))
	else:
		appointment = PatientAppointment.objects.filter(id=pk).first()
		logger.info("Just checking")
		context = {'appointment':appointment}
		return render(request, 'add_treatment.html', context)


@login_required(login_url='home')
@allowed_roles(allowed_roles=['DOCTOR'])
def pat_profile(request, pk):
	try:
		detail=PatientProfile.objects.filter(id=pk).first()
		details=PatientAddress.objects.filter(id=pk).first()
	except:
		logger.error("Not found")
	return render(request, 'pat_profile.html', {"detail":detail,"details":details })
