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
    path("matches/",          views.matches_list,    name="matches_list"),

    # Eksport
    path("export/",           views.export_data,     name="export_data"),
    path("export/csv/",       views.export_csv,      name="export_csv"),
    path("export/xlsx/",      views.export_xlsx,     name="export_xlsx"),
    # Wykresy 
    path("charts/",           views.charts_view,     name="charts"),
    path("charts/png/",       views.chart_png,       name="chart_png"),
    # Import pliku
    path("import/",           views.import_file,     name="import_file"),

    # --- EDYCJA I USUWANIE ---
    path("patient/<int:id>/edit/",     views.edit_patient,      name="edit_patient"),
    path("patient/<int:id>/delete/",   views.delete_patient,    name="delete_patient"),
    
    path("prosthesis/<int:id>/edit/",  views.edit_prosthesis,   name="edit_prosthesis"),
    path("prosthesis/<int:id>/delete/",views.delete_prosthesis, name="delete_prosthesis"),
    
    path("companies/",                 views.companies_list,    name="companies_list"),
    path("company/<int:id>/edit/",     views.edit_company,      name="edit_company"),
    path("company/<int:id>/delete/",   views.delete_company,    name="delete_company"),
]