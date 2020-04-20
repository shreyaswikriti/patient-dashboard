from django.urls import path
from .  import views

urlpatterns = [
    path('/hosp_dash', views.hosp_dash, name='hosp_dash'),
    path('/hospital_profile', views.hospital_profile, name='hospital_profile'),
]
