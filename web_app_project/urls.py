from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('prostheses/', views.prosthesis_list),

    path('patients/', views.patients),
    
    path('patient/<int:id>/', views.patient_profile),

    path('add-patient/', views.add_patient),
    path('add-prosthesis/', views.add_prosthesis),
    path('add-company/', views.add_company),
    path('add-parameter/', views.add_parameter),
    path("add-match/", views.add_match),
]
