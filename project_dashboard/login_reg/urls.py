from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('reg_doc', views.register_doc, name='reg_doc'),
    path('reg_patient', views.register_patient, name='reg_patient'),
    path('reg_hospital', views.register_hospital, name='reg_hospital'),
    path('error', views.error, name='error'),



]
