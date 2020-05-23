from django.db import models
from login_reg.models import User
from hospital.models import hospitalProfile
# Create your models here.

GENDER =(
	('MALE', 'MALE'),
	('FEMALE', 'FEMALE'),
	('OTHERS', 'OTHERS'),)



class DoctorProfile(models.Model):
	firstName = models.CharField(max_length=100, null=False)
	lastName = models.CharField(max_length=100, null=False)
	dob = models.DateField(null=False)
	gender = models.CharField(max_length=100, choices=GENDER)
	timestamp = models.DateTimeField(auto_now_add=True)
	verify  = models.BooleanField(null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	hospital = models.ForeignKey(hospitalProfile, on_delete=models.CASCADE)

	def __str__(self):
		return self.firstName



class DoctorEducation(models.Model):
	college = models.CharField(max_length=255)
	degree = models.CharField(max_length=255)
	doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)


	def __str__(self):
		return self.college


class DoctorSpecialisation(models.Model):
	treatment = models.CharField(max_length=255)
	doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)


	def __str__(self):
		return self.treatment
 
