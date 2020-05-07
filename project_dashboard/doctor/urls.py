from django.urls import path
from . import views
urlpatterns = [
    path('doc_dash/', views.doc_dash, name='doc_dash'),
    path('doctor_profile/', views.doctor_profile, name='doctor_profile'),
]
