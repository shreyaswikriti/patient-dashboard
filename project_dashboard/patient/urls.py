from django.urls import path
from . import views

urlpatterns = [
	path('treatment_list/', views.treatment_list, name='treatment_list'),
    path('patient_detail/<int:pk>', views.patient_detail, name='patient_detail'),
    path('patient_profile/', views.patient_profile, name='patient_profile'),
    path('doctor_search/', views.doctor_search, name='doctor_search'),
    path('all_doctor/', views.all_doctor, name='all_doctor'),
    path('appointment/', views.make_appointment, name='appointment'),
    path('save_appointment/', views.save_appoinment, name='save_appoinment'),
    path('patient_address/<int:pk>', views.patient_address, name='patient_address'),
    path('conf_appointment/', views.conf_appointment, name='conf_appointment'),
    path('all_appointments/', views.all_appointments, name='all_appointments'),
    path('request_appointment/', views.request_appointment, name='request_appointment'),
    path('doc_profile/<int:pk>', views.doc_profile, name='doc_profile')

]
