from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView

from custom_users.forms import RegistrationForm


class Registration(CreateView):
    form_class = RegistrationForm
    success_url = '/users/'
    template_name = 'registration.html'


class NewLoginForm(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('users: users')


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'user_list.html'

