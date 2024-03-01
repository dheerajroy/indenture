from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import AccountCreationForm, CustomLoginForm


class SignUpView(CreateView):
    model = User
    form_class = AccountCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('users:signin')


class SignInView(LoginView):
    template_name = 'signin.html'
    form_class = CustomLoginForm
    # success_url = reverse_lazy('index')
    success_url = '/'


class SignOutView(LogoutView):
    template_name = 'confirm.html'
    success_url = reverse_lazy('users:signin')
