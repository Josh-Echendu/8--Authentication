from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView,ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from .models import Trip, Note

# Create your views here.

class HomeView(TemplateView):
    template_name = 'trip/index.html'

# List the Trips
def trip_list(request):

    # Extract the record associated with the logged in user
    # To get the Trips associated with the logged in user
    if request.user.is_authenticated: 
        trips =  Trip.objects.filter(user_id=request.user)
    else:
        trips = Trip.objects.filter(is_public=True)
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

# To view the Trips
def TripDetail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)

    notes = trip.notes.all()
    context = {
        'trips': trip,
        'notes': notes
    }

    return render(request, 'trip/trip_detail.html', context)

# To view the notes
def NoteDetail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    context = {
        'notes': note
    }

    return render(request, 'trip/note_detail.html', context)

# To list the Notes
class NoteListView(ListView):
    model = Note

    template_name = 'trip/note_list.html'

    # To return all the notes for the logged in user
    # To get the notes associated with the logged in user
    def get_queryset(self):

        # we are filtering these notes based on a Trip field 
        queryset = Note.objects.filter(trip_id__user_id=self.request.user)
        return queryset


    # To create Note
class NoteCreateView(CreateView):
    model = Note

    success_url = reverse_lazy('note-list')
    fields = '__all__'

    # To create note for the logged in user only and to avoid creating note for other users
    def get_form(self): # This get the actual form
        form = super(NoteCreateView, self).get_form() # type: ignore
        
        # Extract the Trips only for the logged in User
        trips = Trip.objects.filter(user_id=self.request.user)

        # To modify a trip on the form
        form.fields['trip_id'].queryset = trips
        return form


#083-Adding a Create Note Form Using Class Based View