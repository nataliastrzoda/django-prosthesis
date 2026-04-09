from django.shortcuts import render
from .models import *

def home(request):
    return render(request, "home.html")

def prosthesis_list(request):
    prostheses = Prosthesis.objects.all()
    return render(request, "prosthesis_list.html", {
        "prostheses": prostheses
    })

def patient_profile(request, id):
    patient = Patient.objects.get(id=id)
    history = PatientProsthesis.objects.filter(patient=patient)

    return render(request, "patient_profile.html", {
        "patient": patient,
        "history": history
    })

def patients(request):
    patients = Patient.objects.all()
    return render(request, "patients.html", {
        "patients": patients
    })


