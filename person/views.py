from django.shortcuts import render, redirect
from django.contrib import messages
from person.forms import UserRegisterForm#, UserAuthForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def register(request):
    if request.user.is_authenticated:
        username=request.user.get_username()
        messages.warning(request, f'You already have an account for {username}!')
        return redirect('home')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can log in now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    pageArray = {'form': form}
    return render(request, 'person/register.html', pageArray)

@login_required
def profile(request):
    return render(request, 'person/profile.html')
