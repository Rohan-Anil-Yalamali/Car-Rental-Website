from django.shortcuts import render

# Create your views here.
import json

file = open(r"E:\Pyspiders Django\car rental\cars\fake_car_rental_data.json", 'r')
json_data = file.read()
py_data = json.loads(json_data)

cars = py_data

def carsview(request):
    return render(request, 'cars.html',)

def cardetail(request, id):
    context = {'car': cars[id-1]}
    return render(request, 'car_detail.html', context)

def home(request):
    context = {'cars': cars}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')