from django import forms
from django.contrib.auth.models import User
from .models import *

class CitaAgregarForm(forms.ModelForm):
    class Meta:
        model = Cita
        exclude = ['usuario', 'created']

    def __init__(self, *args, **kwargs):
        super(CitaAgregarForm, self).__init__(*args, **kwargs)


class CitaEditarForm(forms.ModelForm):
    class Meta:
        model = Cita
        exclude = ['usuario', 'created']

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop("usuario")
        super(CitaEditarForm, self).__init__(*args, **kwargs)