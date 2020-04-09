from django.urls import path
from . import views

urlpatterns = [
    path('patient/', views.patient_detail, name='patient_detail'),
]
