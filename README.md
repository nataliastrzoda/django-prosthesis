# Django Prosthesis System

## Jak uruchomić projekt

### 1. Klonowanie repo
git clone <LINK>
cd prosthesis-system

### 2. Virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Instalacja Django
pip install django

### 4. Migracje
python manage.py makemigrations
python manage.py migrate

### 5. Uruchomienie serwera
python manage.py runserver