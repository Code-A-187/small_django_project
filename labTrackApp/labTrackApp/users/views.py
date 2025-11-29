from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout

from labTrackApp.users.forms import UserRegisterForm



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! You are now able to Log In!")
            return redirect("login-page")
    else:
        form =UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')

    return redirect('home-page')