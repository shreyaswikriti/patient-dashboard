from django.contrib import admin
from .models import DoctorProfile, DoctorSpecialisation, DoctorEducation
# Register your models here.

admin.site.register(DoctorProfile)
admin.site.register(DoctorEducation)
admin.site.register(DoctorSpecialisation)