from django.urls import path
from .  import views

urlpatterns = [
    path('hosp_dash/', views.hosp_dash, name='hosp_dash'),
    path('hospital_profile/', views.hospital_profile, name='hospital_profile'),
    path('hospital_address/<int:pk>', views.hospital_address, name='hospital_address'),
    path('verify_doctor/<int:pk>', views.verify_doctor, name='verify_doctor'),
    path('search_doctor/', views.search_doctor, name='search_doctor'),
]
