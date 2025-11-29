from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register-page'),
    path('login/', auth_views.LoginView.as_view(template_name = "users/login.html"), name='login-page'),
    path('logout/', user_views.logout_user, name='logout'),
]
