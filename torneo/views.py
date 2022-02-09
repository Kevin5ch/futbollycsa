from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
  return render(request,'index.html')

def fixture(request):
  return render(request,'fixture.html')

def posiciones(request):
  return render(request,'posiciones.html')