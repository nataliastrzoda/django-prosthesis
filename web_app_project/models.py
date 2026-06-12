from django.db import models

# Definicje opcji wyboru (Dropdowny)
TYPE_CHOICES = [('Noga', 'Noga'), ('Ręka', 'Ręka')]
SIDE_CHOICES = [('Lewa', 'Lewa'), ('Prawa', 'Prawa')]
LEVEL_CHOICES = [
    ('Udo', 'Udo'),
    ('Podudzie', 'Podudzie'),
    ('Staw biodrowy', 'Staw biodrowy'),
    ('Ramię', 'Ramię'),
    ('Przedramię', 'Przedramię'),
    ('Dłoń', 'Dłoń'),
]
SIZE_CHOICES = [('S', 'S'), ('M', 'M'), ('L', 'L')]

class Company(models.Model):
    name = models.CharField("Nazwa firmy", max_length=200)
    def __str__(self): return self.name

class Prosthesis(models.Model):
    name = models.CharField("Nazwa protezy", max_length=200)
    price = models.FloatField("Cena (zł)")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Firma")
    
    # Nowe parametry protezy
    limb_type = models.CharField("Typ kończyny", max_length=10, choices=TYPE_CHOICES, null=True, blank=True)
    side = models.CharField("Strona", max_length=10, choices=SIDE_CHOICES, null=True, blank=True)
    amputation_level = models.CharField("Poziom amputacji/protezy", max_length=50, choices=LEVEL_CHOICES, null=True, blank=True)
    size = models.CharField("Rozmiar leja", max_length=2, choices=SIZE_CHOICES, null=True, blank=True)

    def __str__(self): return self.name

class Patient(models.Model):
    first_name = models.CharField("Imię", max_length=100)
    last_name = models.CharField("Nazwisko", max_length=100)
    budget = models.FloatField("Budżet (zł)")
    
    # Nowe parametry fizyczne pacjenta
    limb_type = models.CharField("Amputowana kończyna", max_length=10, choices=TYPE_CHOICES, null=True, blank=True)
    side = models.CharField("Strona amputacji", max_length=10, choices=SIDE_CHOICES, null=True, blank=True)
    amputation_level = models.CharField("Poziom amputacji", max_length=50, choices=LEVEL_CHOICES, null=True, blank=True)
    circumference = models.FloatField("Obwód kikuta (cm)", null=True, blank=True)
    size = models.CharField("Rozmiar (obliczony)", max_length=2, choices=SIZE_CHOICES, null=True, blank=True)

    prostheses = models.ManyToManyField(Prosthesis, through="PatientProsthesis", blank=True, verbose_name="Zapisane protezy")
    def __str__(self): return f"{self.first_name} {self.last_name}"

class PatientProsthesis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Pacjent")
    prosthesis = models.ForeignKey(Prosthesis, on_delete=models.CASCADE, verbose_name="Proteza")
    match_score = models.FloatField("Wynik dopasowania (%)", null=True, blank=True)
    doctor_notes = models.TextField("Notatki lekarza", blank=True)

class DoctorForm(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)