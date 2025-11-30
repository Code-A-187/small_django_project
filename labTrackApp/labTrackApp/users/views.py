from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from labTrackApp.users.forms import ProfileEditForm, UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

UserModel = get_user_model()



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


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = "users/profile.html"

    def get_object(self, queryset=None):
        return get_object_or_404(UserModel, pk=self.kwargs['pk'])
    

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')

    return redirect('home-page')

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = "users/profile-edit.html"
    success_url = reverse_lazy('profile-page')

    def test_func(self):
        profile = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        return self.request.user == profile.user
    
    def get_success_url(self):
        return reverse_lazy(
            'profile-page',
            kwargs={
            'pk': self.object.pk
            }
        )


