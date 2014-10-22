from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from accounts.forms import SignUpForm, SignInForm

# Create your views here.
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'accounts/register.html', {'form':form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'accounts/register.html', {'form':form})
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username = username, password = password)
        return render(request, 'accounts/register-ok.html', {'user':user})

@login_required
def profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user':user})
