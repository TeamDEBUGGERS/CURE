from django.shortcuts import render


def index(request):
    return render(request, 'cure/main.html')

def numpad(request):
    return render(request, 'cure/numkeypad.html')

def temp(request):
    return render(request, 'cure/temp.html')