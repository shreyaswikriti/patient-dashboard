from django.urls import path
from . import views

urlpatterns = [
	path('treatment_list/', views.treatment_list, name='treatment_list'),
    path('patient_detail/<int:pk>', views.patient_detail, name='patient_detail'),
    path('patient_profile/', views.patient_profile, name='patient_profile'),
    path('doctor_search/', views.doctor_search, name='doctor_search'),
    path('appointment/', views.make_appointment, name='appointment'),
    path('save_appointment/', views.save_appoinment, name='save_appoinment'),
    path('patient_address/', views.patient_address, name='patient_address'),
    

]
