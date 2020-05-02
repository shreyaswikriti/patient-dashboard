from django.contrib import admin
from . models import PatientProfile, PatientAddress, PatientTreatment, TreatmentComment, PatientAppointment

# Register your models here.


admin.site.register(PatientProfile)
admin.site.register(PatientAddress)
admin.site.register(PatientTreatment)
admin.site.register(TreatmentComment)
admin.site.register(PatientAppointment)