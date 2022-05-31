from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from tables.models import Flight, Plane


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FlightsRoutes(ModelForm):
    class Meta:
        model = Flight
        fields = ('plane_id', 'date', 'name')
        widgets = {
            'date': DateInput(),
        }


class PlanesForm(ModelForm):
    class Meta:
        model = Plane
        fields = ('type',)
