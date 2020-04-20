from django.urls import path
from . import views

urlpatterns = [
    path('/patient_detail', views.patient_detail, name='patient_detail'),
    path('/patient_profile', views.patient_profile, name='patient_profile'),
]
