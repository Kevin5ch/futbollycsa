from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
  return render(request,'index.html')

def fixture(request):
  return render(request,'fixture.html')

def posiciones(request):
  return render(request,'posiciones.html')

def resultados(request):
  return render(request,'resultados.html')

def blog(request):
  return render(request,'blog.html')

def torneo(request):
  return render(request,'torneo.html')