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


class MySignUpView(generic.CreateView):  # jetzt zu mein SignupViw verandern
    form_class = MySignUpForm  # eigen Form erstellen und dann darauf anpasse, imports bedenken
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class MyLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        """Security check complete. Log the user in. PERFORM CUSTOM CODE."""
        auth_login(self.request, form.get_user())
        # form.get_user().execute_after_login()  # Custom code
        return HttpResponseRedirect(self.get_success_url())
