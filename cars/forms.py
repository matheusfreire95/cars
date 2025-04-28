from django import forms

from .models import Brand

class CarForm(forms.Form):
    model = forms.CharField()
    brand = forms.ChoiceField(Brand.objects.all())
