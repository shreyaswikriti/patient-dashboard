from django.shortcuts import render, redirect

from login_reg.decorators import allowed_roles
from doctor.models import DoctorProfile
from .models import hospitalProfile, hospitalAddress
import logging
from login_reg.views import home
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages


logger = logging.getLogger(__name__)
# Create your views here.

@login_required(login_url='home')
@allowed_roles(allowed_roles=['HOSPITAL'])
def hosp_dash(request):
	hospital = hospitalProfile.objects.filter(user=request.user).first()
	if hospital is None:
		logger.error("There is no hospital")
		redirect('error')
	doctors = DoctorProfile.objects.filter(hospital=hospital).order_by('timestamp')
	if doctors is None:
		logger.info("There is no Doctor")
	context  = {'doctors':doctors,'hospital':hospital}
	return render(request, 'hospital_dashboard.html', context)



@login_required(login_url='home')
@allowed_roles(allowed_roles=['HOSPITAL'])
def hospital_profile(request):
	try:
		hdetail=hospitalProfile.objects.filter(user=request.user).first()
		logger.info("Name:{} registrationid: {} and dateofregistration: {}".format(hdetail.name, hdetail.registrationid, hdetail.dateofreg))
		hdetails=hospitalAddress.objects.filter(user=request.user).first()
		logger.info("Address:{} city:{} District: {} Locality: {} State: {} Pincode: {} Nationality: {} contactno:{}".format(hdetails.Address, hdetails.city, hdetails.district, hdetails.locality,hdetails.state,hdetails.pincode,hdetails.nationality,hdetails.contactno))
	except:
		logger.error("oject not found")
	return render(request, 'hospital_profile.html', {"hdetail":hdetail,"hdetails":hdetails })


@login_required(login_url='home')
@allowed_roles(allowed_roles=['HOSPITAL'])
def hospital_address(request, pk):
	logger.info('Saving address')
	if request.method=='POST':
		try:
			logger.info("HOSPITAL Name")
			name = request.POST['name']
			logger.info(name)
			registrationid = request.POST['registrationid']
			logger.info(registrationid)
			dateofregistration=request.POST['dateofregistration']
			logger.info(dateofregistration)
			address = request.POST['add']
			logger.info(address)
			city = request.POST['city']
			logger.info(city)
			district = request.POST['dist']
			logger.info(district)
			locality = request.POST['locality']
			logger.info(locality)
			state = request.POST['state']
			logger.info(state)
			pincode = request.POST['pincode']
			logger.info(pincode)
			nationality = request.POST['nationality']
			logger.info(nationality)
			contact = request.POST['phone']
			logger.info(contact)
			temp_date = datetime.strptime(dateofregistration, "%m/%d/%Y").date()
			logger.info(temp_date)
		except:
			logger.error("User address not created")
		hospitalProfile.objects.filter(user=request.user).update(name =name,
			registrationid=registrationid,
			dateofreg=temp_date)
		hospitalAddress.objects.filter(id=pk).update(Address=address,
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
		return redirect('hospital_profile')
	else:
		hospital = hospitalProfile.objects.filter(user=request.user).first()
		Address = hospitalAddress.objects.filter(id=pk).first()
		context = {'hospital':hospital,'Address':Address}
		return render(request,'hospital_address.html',context)



@login_required(login_url='home')
@allowed_roles(allowed_roles=['HOSPITAL'])
def verify_doctor(request, pk):
	if request.method=='POST':
		status = request.POST['status']
		if status == 'True':
			DoctorProfile.objects.filter(id=pk).update(verify=True)
			messages.success(request, "You have verified your doctor")
		else:
			DoctorProfile.objects.filter(id=pk).update(verify=False)
			messages.success(request, "You have cancel verification of your doctor")
		return redirect('hosp_dash')
	else:
		hospital = hospitalProfile.objects.filter(user=request.user).first()
		if hospital is None:
			logger.error("There is no hospital")
			redirect('error')
		doctor = DoctorProfile.objects.filter(id=pk).first()
		if doctor is None:
			logger.info("There is no Doctor")
		context  = {'doctor':doctor,'hospital':hospital}
		return render(request, 'verification.html', context)




def search_doctor(request):
	query = request.GET['query']
	hospital = hospitalProfile.objects.filter(user=request.user).first()
	if hospital is None:
		logger.error("There is no hospital")
		redirect('error')
	doctors = DoctorProfile.objects.filter(firstName__icontains=query, hospital=hospital)
	context  = {'doctors':doctors,'hospital':hospital}
	return render(request, 'hospital_dashboard.html', context)