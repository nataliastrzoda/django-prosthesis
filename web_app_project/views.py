from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *


def home(request):
    from .models import Patient, Prosthesis, Company, PatientProsthesis

    companies = Company.objects.all()
    chart_labels = [c.name for c in companies]
    chart_data   = [Prosthesis.objects.filter(company=c).count() for c in companies]

    return render(request, "home.html", {
        "patient_count":    Patient.objects.count(),
        "prosthesis_count": Prosthesis.objects.count(),
        "company_count":    Company.objects.count(),
        "match_count":      PatientProsthesis.objects.count(),
        "chart_labels":     chart_labels,
        "chart_data":       chart_data,
    })

def prosthesis_list(request):
    prostheses = Prosthesis.objects.all()
    return render(request, "prosthesis_list.html", {"prostheses": prostheses})


def patient_profile(request, id):
    patient = Patient.objects.get(id=id)
    history = PatientProsthesis.objects.filter(patient=patient)

    return render(
        request, "patient_profile.html", {"patient": patient, "history": history}
    )


def patients(request):
    patients = Patient.objects.all()
    return render(request, "patients.html", {"patients": patients})


def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pacjent zapisany poprawnie!")
            return redirect("/")
    else:
        form = PatientForm()

    return render(request, "add_patient.html", {"form": form})


def add_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Firma zapisana poprawnie!")
            return redirect("/")
    else:
        form = CompanyForm()

    return render(request, "add_company.html", {"form": form})


def add_parameter(request):
    if request.method == "POST":
        form = ParameterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Parametr zapisany poprawnie!")
            return redirect("/")
    else:
        form = ParameterForm()

    return render(request, "add_parameter.html", {"form": form})


def add_prosthesis(request):
    if request.method == "POST":
        form = ProsthesisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proteza zapisana poprawnie!")
            return redirect("/")
    else:
        form = ProsthesisForm()

    return render(request, "add_prosthesis.html", {"form": form})


def add_match(request):
    if request.method == "POST":
        form = PatientProsthesisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/patients/")
    else:
        form = PatientProsthesisForm()

    return render(request, "add_match.html", {"form": form})
