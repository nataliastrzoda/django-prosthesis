from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('prostheses/', views.prosthesis_list),

    path('patients/', views.patients),
    
    path('patient/<int:id>/', views.patient_profile),
]
