from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm

def index(request):
    form = UserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'member/index.html', context=context)