from django import forms
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.conf import path
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm, ProfileImageForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


class UserRegister(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        contex = {
            'form':form
        }
        return render(request, self.template_name ,contex)


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user = Profile.objects.create(user=user)
            messages.success(request, 'You registered successfully', 'success')
            return redirect('core:home')
        return render(request, self.template_name, {'form': form} )   


class UserLogin(View):
    form_class = UserLoginForm
    tempalte_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.tempalte_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You Logged in seccessfully', 'success')
                return redirect('core:home')
            messages.error(redirect, 'Your Username or Password is Wrong', 'danger')
        return render(request, self.tempalte_name, {'form': form})


class UserLogout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You loggedout successfully', 'info')
        return redirect('core:home')


class UserDashboard(LoginRequiredMixin, View):
    template_name = 'accounts/dashboard.html'
    form_class = ProfileImageForm

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        return render(request, self.template_name, {'user': user, 'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Uploade successfully', 'success')
            return redirect('accounts:dashboard', request.user.username)