from django import forms
from .models import Trip,Car

class TripRequestForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields ="__all__" 
        
# Register a user
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# add a trip
class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = "__all__"
        


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"