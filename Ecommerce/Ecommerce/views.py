from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'shop/home.html')

