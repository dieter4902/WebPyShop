from django import forms
from django.contrib.auth import (
    login as auth_login,
)
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
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

class MyUserListView(generic.ListView):
    model = MyUser
    context_object_name = 'all_myusers'
    template_name = 'myuser-list.html'
    
def userProfile(request):
    context = {'myuser': request.user}
    return render(request, 'myuser-profile.html', context)