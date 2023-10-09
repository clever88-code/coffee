from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib import messages
from django.views.generic import FormView

from .forms import RecordForm

def index(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Запись добавлена')
            form.save()
            

    else:
        form = RecordForm()

    return render(request, 'main/index.html', {'form': form})