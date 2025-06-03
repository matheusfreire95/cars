from django import forms
from .models import Brand, Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car 
        fields = '__all__'
