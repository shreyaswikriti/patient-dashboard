from django.shortcuts import render

from login_reg.decorators import allowed_roles
# Create your views here.

# @allowed_roles(allowed_roles=['HOSPITAL'])
def hosp_dash(request):
	return render(request, 'hospital_dashboard.html', {})



def hospital_profile(request):
	return render(request, 'hospital_profile.html', {})