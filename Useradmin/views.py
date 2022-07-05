from django.contrib.auth import (
    login as auth_login,
)
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from .forms import MySignUpForm
from .models import MyUser


class SignUp(generic.CreateView):  # jetzt zu mein SignupViw verandern
    form_class = MySignUpForm  # eigen Form erstellen und dann darauf anpasse, imports bedenken
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
