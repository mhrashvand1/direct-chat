from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from account.forms import SignUpForm, LoginForm, ProfileForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

class SignUpView(View):
    
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'account/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('core:chat')   
        return render(request, 'account/signup.html', {'form': form})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.cleaned_data.get("user"))
            return redirect(self.get_redirect_url())  
        return render(request, 'account/login.html', {'form': form})

    def get_redirect_url(self):
        redirect_url = self.request.GET.get("redirect_url")
        return redirect_url if redirect_url else "core:chat"


class LogoutView(View):
   
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse("You are not logged in.")
        return super().dispatch(request, *args, **kwargs)
      
    def get(self, request, *args, **kwargs):
        logout(request=request)
        return redirect("account:login")
    
      
class ProfileView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(
                reverse("account:login") + "?redirect_url=account:profile"
            )
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = ProfileForm(instance=request.user)
        return render(request, 'account/profile.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'account/profile.html', {'form': form})
