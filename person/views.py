from django.shortcuts import render, redirect
from django.contrib import messages
from person.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Updated Successfully')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    pageArray = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'person/profile.html', pageArray)
