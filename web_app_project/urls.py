from django.urls import path
from . import views

urlpatterns = [
    path("",                  views.home,            name="home"),
    path("prostheses/",       views.prosthesis_list, name="prosthesis_list"),
    path("patients/",         views.patients,        name="patients"),
    path("patient/<int:id>/", views.patient_profile, name="patient_profile"),
    path("add-patient/",      views.add_patient,     name="add_patient"),
    path("add-prosthesis/",   views.add_prosthesis,  name="add_prosthesis"),
    path("add-company/",      views.add_company,     name="add_company"),
    path("add-parameter/",    views.add_parameter,   name="add_parameter"),
    path("add-match/",        views.add_match,       name="add_match"),
]
