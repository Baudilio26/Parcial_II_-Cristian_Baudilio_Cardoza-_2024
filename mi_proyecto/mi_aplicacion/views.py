from django.shortcuts import render

def index(request):
    return render(request, 'mi_aplicacion/index.html')