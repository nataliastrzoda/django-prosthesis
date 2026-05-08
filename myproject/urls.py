from django.contrib import admin
from django.urls import path, include   # ← dodaj include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("web_app_project.urls")),   # ← DODAJ TO (bez tego żadna strona nie działa!)
]