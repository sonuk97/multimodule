from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add_doctor',views.add_doctor,name='add_doctor'),
    path('add_patient',views.add_patient,name='add_patient'),
    path('log_in',views.log_in,name='log_in'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('doctor_home',views.doctor_home,name='doctor_home'),
    path('patient_home',views.patient_home,name='patient_home'),
    path('patient_signup',views.patient_signup,name='patient_signup'),
    path('doctor_signup',views.doctor_signup,name='doctor_signup'),
    path('login1',views.login1,name='login1'),
    path('log_out',views.log_out,name='log_out'),
    
]
