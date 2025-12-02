from django.urls import path
from . import views

urlpatterns = [
    path('', views.InstrumentListView.as_view(), name='instruments-page'),
    ]