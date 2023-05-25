from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *

class TripListView(ListView):
	model = Trip
	
class TripUpdateView(UpdateView):
	model = Trip
	fields = ["traveller", "destination", "name","description", "cost"]
	success_url = "/"
	
class TripCreateView(CreateView):
	model = Trip
	fields = ["traveller", "destination", "name", "description", "cost"]
	success_url = "/"
	
class TripDeleteView(DeleteView):
	model = Trip
	success_url = "/"
	

class TravellerListView(ListView):
	model = Traveller
	
class TravellerUpdateView(UpdateView):
	model = Traveller
	fields = ["first_name", "last_name", "email"]
	success_url = "/"
	
class TravellerCreateView(CreateView):
	model = Traveller
	fields = ["first_name", "last_name", "email"]
	success_url = "/"
	
class TravellerDeleteView(DeleteView):
	model = Traveller
	success_url = "/"


class DestinationListView(ListView):
	model = Destination
	
class DestinationUpdateView(UpdateView):
	model = Destination
	fields = ["name", "description"]
	success_url = "/"
	
class DestinationCreateView(CreateView):
	model = Destination
	fields = ["name","description"]
	success_url = "/"
	
class DestinationDeleteView(DeleteView):
	model = Destination
	success_url = "/"


