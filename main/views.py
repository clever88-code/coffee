from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group

from django.views.generic import FormView

from .forms import RecordForm

def index(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            # После успешного сохранения можно выполнить какие-либо дополнительные действия, например, перенаправить на другую страницу
            return redirect('success_url')  # Замените 'success_url' на URL, куда вы хотите перенаправить после успешного сохранения

    else:
        form = RecordForm()

    return render(request, 'main/index.html', {'form': form})