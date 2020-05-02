from django.db import models
from login_reg.models import User
from doctor.models import DoctorProfile
# Create your models here.


GENDER =(
	('MALE', 'MALE'),
	('FEMALE', 'FEMALE'),
	('OTHERS', 'OTHERS'),)


class PatientProfile(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	dob = models.DateField(null=False)
	gender = models.CharField(max_length=100, choices=GENDER)
	user = models.OneToOneField(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.firstName




class PatientAddress(models.Model):
	Address = models.CharField(max_length=255, null =False)
	city = models.CharField(max_length=100, null=False)
	district = models.CharField(max_length=100, null=False)
	locality = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	pincode = models.CharField(max_length=100, null=False)
	nationality = models.CharField(max_length=200, null=False)
	contactno = models.CharField(max_length=10)
	user = models.OneToOneField(User, on_delete=models.CASCADE)



class PatientTreatment(models.Model):
	diagnosis = models.CharField(max_length=1000)
	prescription = models.TextField()
	count = models.IntegerField()
	active = models.BooleanField()
	last_edited = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField()
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
	doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)


class TreatmentComment(models.Model):
	comment = models.CharField(max_length=255)
	timestamp = models.DateTimeField(auto_now_add=True)
	doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
	treatment = models.ForeignKey(PatientTreatment, on_delete=models.CASCADE)




STATUS = (('CONFIRMED', 'CONFIRMED'),
	('REQUESTED', 'REQUESTED'),
	('NA','NA'))
class PatientAppointment(models.Model):
	status = models.CharField(max_length=100, choices=STATUS)
	appointment = models.DateTimeField(auto_now_add=False)
	user = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
	doctor =models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
	timestamp= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.status
