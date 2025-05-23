from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import home_redirect , logout_view

app_name = 'authentication'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='authentication:login'), name='logout'),  
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('/home', home_redirect, name='home'),
]
