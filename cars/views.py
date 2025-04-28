from django.shortcuts import render

from .models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(brand__name__icontains=search)

    return render(request, "cars.html", {"cars": cars})

def new_car_view(request):
    return render(request, "new_car.html")
