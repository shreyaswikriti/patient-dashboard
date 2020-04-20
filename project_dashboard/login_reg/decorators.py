from django.shortcuts import redirect
from django.http import HttpResponse
from . models import *

def unathenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func




def allowed_roles(allowed_roles=[]):
	def decorators(view_func):
		def wrapper_func(request, *args, **kwargs):
			roles = UserRoles.objects.filter(user=request.user).first().roles
			if roles in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return redirect('home')
		return wrapper_func
	return decorators