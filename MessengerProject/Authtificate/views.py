from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from django.views import View
from . import forms


class RegisterViews(View):

    def get(self, request):
        form = forms.CreatUserForm()
        return render(request, "Auth/register.html", {"form":form})
    
    def post(self, request):
        form = forms.CreatUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main")
        return redirect("register")

class LoginViews(View):

    def get(self, request):
        form = forms.AuthenticationForm()
        return render(request, "Auth/login.html", {"form":form})
    
    def post(self, request):
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("main")
        return redirect("login")

def user_logout(request):
    logout(request)
    return redirect("main")