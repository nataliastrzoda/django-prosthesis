from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Parameter(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Prosthesis(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    parameters = models.ManyToManyField(
        Parameter,
        through="ProsthesisParameter"
    )

    def __str__(self):
        return self.name


class ProsthesisParameter(models.Model):
    prosthesis = models.ForeignKey(Prosthesis, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    budget = models.FloatField()

    prostheses = models.ManyToManyField(
        Prosthesis,
        through="PatientProsthesis"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PatientProsthesis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prosthesis = models.ForeignKey(Prosthesis, on_delete=models.CASCADE)

    match_score = models.FloatField(null=True, blank=True)
    doctor_notes = models.TextField(blank=True)


class DoctorForm(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)