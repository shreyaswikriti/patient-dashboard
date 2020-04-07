from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
	logger.warning("Your log message is here")
	logger.info("Hello My Dear")
	return render(request, 'hello.html', {})