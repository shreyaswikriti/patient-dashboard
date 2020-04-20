from django.contrib import admin
from .models import hospitalProfile, hospitalAddress

# Register your models here.
admin.site.register(hospitalProfile)
admin.site.register(hospitalAddress)