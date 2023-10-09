from django import forms
from django.core.exceptions import ValidationError
from requests import request

from .models import Record




class RecordForm(forms.ModelForm):
    success_url = '/record'
    class Meta:
        model = Record
        fields = ['name', 'email', 'number']
