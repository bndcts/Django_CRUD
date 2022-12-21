from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import User


def home(request):
    return HttpResponse("Coding challenge for SUMM")

class UserList(ListView):
    model = User

class UserView(DetailView):
    model = User

class UserCreate(CreateView):
    model = User
    fields = ["Id", "Name", "QuotaSpent", "QuotaLimit"]
    success_url = reverse_lazy("user_list")

class UserUpdate(UpdateView):
    model = User
    fields = ['Id', 'Name', 'QuotaSpent', 'QuotaLimit']
    success_url = reverse_lazy("user_list")

class UserDelete(DeleteView):
    model = User
    fields = ['Id', 'Name', 'QuotaSpent', 'QuotaLimit']
    success_url = reverse_lazy("user_list")