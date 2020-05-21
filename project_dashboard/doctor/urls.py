from django.urls import path
from . import views
urlpatterns = [
    path('doc_dash/', views.doc_dash, name='doc_dash'),
    path('doctor_profile/', views.doctor_profile, name='doctor_profile'),
    path('requested_appointment/', views.requested_appointment, name='requested_appointment'),
    path('update_appointment/', views.update_appointment, name='update_appointment'),
    path('all_appointment/', views.all_appointment, name='all_appointment'),
    path('confirmed_appointment/', views.confirmed_appointment, name='confirmed_appointment'),
    path('patient_treatment/<int:pk>', views.patient_treatment, name='patient_treatment'),
    path('treatment_detail/<int:pk>',views.treatment_detail, name='treatment_detail'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('edit_treatment/', views.edit_treatment, name='edit_treatment'),
    path('add_treatment/<int:pk>', views.add_treatment, name='add_treatment'),
    path('update_specialisation/<int:pk>', views.update_specialisation, name='update_specialisation'),
    path('update_college/<int:pk>', views.update_college, name='update_college'),
    path('add_college/', views.add_college, name='add_college'),
    path('add_spec/', views.add_spec, name='add_spec'),
]
