from django.forms import ModelForm
from .models import *


class BootstrapMixin:
    """Mixin dodający klasę Bootstrap do wszystkich pól formularza."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            current = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (current + " form-control").strip()


class PatientForm(BootstrapMixin, ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class ProsthesisForm(BootstrapMixin, ModelForm):
    class Meta:
        model = Prosthesis
        fields = "__all__"


class CompanyForm(BootstrapMixin, ModelForm):
    class Meta:
        model = Company
        fields = "__all__"


class ParameterForm(BootstrapMixin, ModelForm):
    class Meta:
        model = Parameter
        fields = "__all__"


class PatientProsthesisForm(BootstrapMixin, ModelForm):
    class Meta:
        model = PatientProsthesis
        fields = "__all__"


class DoctorFormForm(BootstrapMixin, ModelForm):
    class Meta:
        model = DoctorForm
        fields = "__all__"