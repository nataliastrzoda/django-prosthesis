from django.http import HttpResponse

def mypage1(request):
    return HttpResponse("Strona pierwsza...")