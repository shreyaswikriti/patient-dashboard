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
]
