from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Instrument


class InstrumentListView(ListView):
    model = Instrument
    template_name = 'instruments/instruments-list.html'
    context_object_name = 'instruments'
    paginate_by = 6

class InstrumentDetailView(DetailView):
    model = Instrument
    template_name= 'instruments/unstrument-details'
    context_object_name = 'instrument'

