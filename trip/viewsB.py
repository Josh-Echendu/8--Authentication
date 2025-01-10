from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Trip, Note  

# Create your views here.

class HomeView(TemplateView):
    template_name = 'trip/index.html'

def trip_list(request):

    # Extract the record associated with each user
    trips =  Trip.objects.all()

    context = {
        'trips': trips
    }
    return render(request, "trip/trip_list.html", context)
