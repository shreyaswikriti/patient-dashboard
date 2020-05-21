from django.shortcuts import render, redirect
from login_reg.decorators import allowed_roles
from .models import PatientProfile, PatientTreatment, TreatmentComment, PatientAppointment, PatientAddress
from doctor.models import DoctorSpecialisation, DoctorProfile, DoctorEducation
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from login_reg.views import home
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
import logging

logger = logging.getLogger(__name__)

@login_required(login_url='home')
@allowed_roles(allowed_roles=['PATIENT'])
def treatment_list(request):
	# logger.info("Requesting for registration or Login Page")
	patient = PatientProfile.objects.filter(user=request.user).first()
	if patient is None:
		logger.error("Patient not found")
		redirect('error')
	treatments = PatientTreatment.objects.filter(patient=patient, parent_treatment__isnull=True).order_by('last_edited')
	if treatments is None:
		logger.info("Patient was never diagnised")
	count = PatientAppointment.objects.filter(status='CONFIRMED', user=patient).order_by('appointment').count()
	appointments = PatientAppointment.objects.filter(status='CONFIRMED', user=patient).order_by('appointment')[:6]
	context = {'treatments': treatments, 'patient':patient, 'appointments':appointments, 'count':count}
	return render(request, 'patient_dashboard.html', context)




@login_required(login_url='home')
@allowed_roles(allowed_roles=['PATIENT'])
def patient_profile(request):
	try:
		detail=PatientProfile.objects.filter(user=request.user).first()
		logger.info("Name:{} {} dob: {} and Gender: {}".format(detail.firstName, detail.lastName, detail.dob, detail.gender))
		details=PatientAddress.objects.filter(user=request.user).first()
		logger.info("Address:{} city:{} District: {} Locality: {} State: {} Pincode: {} Nationality: {} contactno:{}".format(details.Address, details.city, details.district, details.locality,details.state,details.pincode,details.nationality,details.contactno))
	except:
		logger.error("oject not found")
	return render(request, 'patient_profile.html', {"detail":detail,"details":details }) 


@login_required(login_url='home')
@allowed_roles(allowed_roles=['PATIENT'])
def patient_detail(request, pk):
	if request.method=='POST':
		try:
			rate = int(request.POST['quantity'])
		except:
			logger.error("ratting has not been submitted")
		PatientTreatment.objects.filter(id=pk).update(rating=rate)
		rating = PatientTreatment.objects.filter(id=pk).first().rating
		messages.success(request,("You have added {} rating".format(rating)))
		return HttpResponseRedirect(reverse('patient_detail', args=(pk,)))
	else:
		treatment = PatientTreatment.objects.filter(id=pk).first()
		if treatment is None:
			logger.error("Treatment does not exist")
			redirect('error')
		comments = TreatmentComment.objects.filter(treatment=treatment).order_by('timestamp')
		if comments is None:
			logger.info("No comments available")
		context = {'comments':comments, 'treatment':treatment}
		return render(request, 'patient_detail.html', context)


	


@login_required(login_url='home')
@allowed_roles(allowed_roles=['PATIENT'])
def doctor_search(request):
	query = request.GET['query']
	rs = DoctorSpecialisation.objects.filter(treatment__icontains=query)
	context = {'rs':rs}
	return render(request, 'doctor_search.html', context)

@login_required(login_url='home')
@allowed_roles(allowed_roles=['PATIENT'])
def make_appointment(request):
	doc = request.POST['doctor']
	logger.info("Doctor with id {} got request for appointment".format(doc))
	doctor = DoctorProfile.objects.filter(id=doc).first()
	treatment = DoctorSpecialisation.objects.filter(doctor=doctor)
	context = {'doctor':doctor, 'treatment':treatment}
	return render(request, 'appointment.html', context)


@login_required(login_url='home')
@allowed_roles(allowed_roles=['PATIENT'])
def save_appoinment(request):
	logger.info('Saving appointment')
	try:
		doc = request.POST['doc_id']
		treatment = request.POST['treatment']
		appointmenttime = request.POST['appointmenttime']
		status =  request.POST['status'].upper()
		logger.info('Requested for the appoinmenttime {} {} {} {}'.format(doc, appointmenttime, treatment, status))
		temp_date = datetime.strptime(appointmenttime, "%m/%d/%Y").date()
	except:
		logger.info("Field were invalid")
	logger.info("We got the"+ doc)
	doctor = DoctorProfile.objects.filter(id=doc).first()
	patient = PatientProfile.objects.filter(user=request.user).first()
	PatientAppointment.objects.create(doctor=doctor,
		user=patient,
		appointment=temp_date,
		status=status)
	messages.success(request, ("Your appointment has been made"))
	return redirect('home')



@login_required(login_url='home')
@allowed_roles(allowed_roles=['PATIENT'])	
def patient_address(request, pk):
	logger.info('Saving address')
	if request.method=='POST':
		try:
			first = request.POST['first']
			last = request.POST['last']
			address = request.POST['add']
			city = request.POST['city']
			district = request.POST['dist']
			locality = request.POST['locality']
			state = request.POST['state']
			pincode = request.POST['pincode']
			nationality = request.POST['nationality']
			contact = request.POST['phone']
		except:
			logger.error("User address not created")
		PatientProfile.objects.filter(user=request.user).update(firstName =first,
			lastName=last)
		PatientAddress.objects.filter(id=pk).update(Address=address,
			city=city,
			district=district,
			locality=locality,
			state=state,
			pincode=pincode,
			nationality=nationality,
			contactno=contact,
			user=request.user)
		logger.info("User address added")
		messages.success(request,("You have added your address"))
		return redirect('patient_profile')
	else:
		patient = PatientProfile.objects.filter(user=request.user).first()
		Address = PatientAddress.objects.filter(id=pk).first()
		context = {'patient':patient,'Address':Address}
		return render(request,'patient_address.html',context)
 
		   
@login_required(login_url='home')
@allowed_roles(allowed_roles=['PATIENT'])
def conf_appointment(request):
	patient = PatientProfile.objects.filter(user=request.user).first()
	appointments = PatientAppointment.objects.filter(status='CONFIRMED', user=patient).order_by('appointment')
	context = {'appointments':appointments}
	return render(request, 'conf_appointment.html', context)


@login_required(login_url='home')
@allowed_roles(allowed_roles=['PATIENT'])
def request_appointment(request):
	patient = PatientProfile.objects.filter(user=request.user).first()
	appointments = PatientAppointment.objects.filter(status='REQUESTED', user=patient).order_by('appointment')
	context = {'appointments':appointments}
	return render(request, 'request_appointment.html', context)


@login_required(login_url='home')
@allowed_roles(allowed_roles=['PATIENT'])
def all_appointments(request):
	patient = PatientProfile.objects.filter(user=request.user).first()
	appointments = PatientAppointment.objects.filter(user=patient).order_by('appointment')
	context = {'appointments':appointments}
	return render(request, 'all_appointments.html', context)

@login_required(login_url='home')
@allowed_roles(allowed_roles=['PATIENT'])
def doc_profile(request, pk):
	try:
		prof = DoctorProfile.objects.filter(id=pk).first()
		educs = DoctorEducation.objects.filter(doctor=prof)
		specs = DoctorSpecialisation.objects.filter(doctor=prof)
	except:
		logger.error("object not found")
	context = {'prof':prof,'educs':educs,'specs':specs}
	return render(request,'doc_profile.html',context)



		

	    
	
	
	
		
	