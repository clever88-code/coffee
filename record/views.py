from django.shortcuts import render
from django import forms
from record.forms import RecordForm
from django.views.generic import ListView, DetailView, CreateView, TemplateView
# Create your views here.
from .forms import RecordForm

def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            

    else:
        form = RecordForm()

    return render(request, 'add_record.html', {'form': form})