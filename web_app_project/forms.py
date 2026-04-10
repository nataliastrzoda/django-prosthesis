from django.forms import ModelForm
from .models import *

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class ProsthesisForm(ModelForm):
    class Meta:
        model = Prosthesis
        fields = '__all__'


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class ParameterForm(ModelForm):
    class Meta:
        model = Parameter
        fields = "__all__"


class PatientProsthesisForm(ModelForm):
    class Meta:
        model = PatientProsthesis
        fields = '__all__'


class DoctorFormForm(ModelForm):
    class Meta:
        model = DoctorForm
        fields = '__all__'