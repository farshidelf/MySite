from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth import login, authenticate


def index(request):
    form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'member/index.html', context=context)


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'member/register.html'
    success_url = reverse_lazy('member:index')
    success_message = 'Successfully Registered'

    def get_success_url(self):
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        
        return super().get_success_url()

    

    



