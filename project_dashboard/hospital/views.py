from django.shortcuts import render, redirect

from login_reg.decorators import allowed_roles
from doctor.models import DoctorProfile
from .models import hospitalProfile, hospitalAddress
import logging
from login_reg.views import home
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)
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
			name = request.POST['name']
			registrationid = request.POST['registrationid']
			dateofregistration=request.POST['dateofregistration']
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
		hospitalProfile.objects.filter(user=request.user).update(name =name,
			registrationid=registrationid,
			dateofregistration=dateofregistration)
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
