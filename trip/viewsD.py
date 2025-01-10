from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from .models import Trip, Note

# Create your views here.

class HomeView(TemplateView):
    template_name = 'trip/index.html'

def trip_list(request):

    # Extract the record associated with the logged in user
    trips =  Trip.objects.filter(user_id=request.user)
    context = {
        'trips': trips
    }
    return render(request, "trip/trip_list.html", context)


# Allow user to create a trip i.e to add a form
class TripCreateView(CreateView):
    model = Trip

    # Where to go after successfull creation
    success_url = reverse_lazy('trip-list')

    # fields
    fields = ['city', 'country', 'start_date', 'end_date']

    template_name = 'trip/trip_form.html'

    # This method would get triggerd any time the form is submitted to create a new Trip
    def form_valid(self, form):

        # we want it that when we add or create a new trip we want to assign the new trip(form) to the current logged in user
        form.instance.user_id = self.request.user # we are assigning the user_id value to the current logged in user 

        return super().form_valid(form) 

def TripDetail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)

    notes = trip.notes.all()
    context = {
        'trips': trip,
        'notes': notes
    }

    return render(request, 'trip/trip_detail.html', context)

def NoteDetail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    context = {
        'note': note
    }

    return render(request, 'trip/note_detail.html', context)

# 081-Creating Notes via Admin and Seeing Notes Details