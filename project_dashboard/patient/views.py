from django.shortcuts import render

# Create your views here.
import logging

logger = logging.getLogger(__name__)

def patient_detail(request):
	logger.info("Requesting for registration or Login Page")
	return render(request, 'base.html', {})
