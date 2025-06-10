from .models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)
        
        return cars


class CarsDetailView(DetailView):
    model = Car
    template_name = 'detail_car.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarsCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarsUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'edit_car.html'

    def get_success_url(self):
        return reverse_lazy('detail_car', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarsDeleteView(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '/'

