from django import forms
from .models import *

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name']

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name']

class Trainer_typeForm(forms.ModelForm):
    class Meta:
        model = Trainer_type
        fields = ['name']

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['name','types','location','state', 'address', 'time']

        widgets = {
            'time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }