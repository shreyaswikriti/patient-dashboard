from django.shortcuts import render
from login_reg.decorators import allowed_roles
# Create your views here.


# @allowed_roles(allowed_roles=['DOCTOR'])
def doc_dash(request):
	return render(request, 'doctor_dashboard.html', {})




def doctor_profile(request):
	return render(request, 'doctor_profile.html', {})