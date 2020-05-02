from django.db import models
from login_reg.models import User

# Create your models here.

TYPE =(
	("GOVERNMENT", "GOVERNMENT"),
	("PRIVATE", "PRIVATE"),
	)

class hospitalProfile(models.Model):
	registrationid = models.CharField(max_length=255)
	name = models.CharField(max_length=200)
	dateofreg = models.DateField(null=True)
	tyep = models.CharField(max_length=50, choices= TYPE)
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)




class hospitalAddress(models.Model):
	Address = models.CharField(max_length=255, null =False)
	city = models.CharField(max_length=100, null=False)
	district = models.CharField(max_length=100, null=False)
	locality = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	pincode = models.CharField(max_length=100, null=False)
	nationality = models.CharField(max_length=200, null=False)
	contactno = models.CharField(max_length=10)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
