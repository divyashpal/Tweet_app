from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.\
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    #reverse_lazy won't get executed until the user hit signup button in reverse() it would take user to login page even user hasn't hit signup button
    template_name = 'accounts/signup.html'