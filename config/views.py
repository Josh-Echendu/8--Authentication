from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout

class SignupView(CreateView):
    form_class = UserCreationForm # we are creating a form
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def logout_view(request):
        if request.method == "POST":
            logout(request) # Logout the user
            return render(request, 'registration/log_out.html')     
        
