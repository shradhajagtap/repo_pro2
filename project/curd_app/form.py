from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control"}),
            "car_company": forms.TextInput(attrs={"class": "form-control"}),
            "car_name_mode": forms.Select(attrs={"class": "form-control"}),
            "car_model_mode": forms.Select(attrs={"class": "form-control"}),
            "car_capacity": forms.TextInput(attrs={"class": "form-control"}),
            "car_cc": forms.TextInput(attrs={"class": "form-control"})

        }

