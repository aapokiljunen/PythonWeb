from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *

class SongListView(ListView):
	model = Song

class SongCreateView(CreateView):
	model = Song
	fields = ["name", "length"]
	success_url = "/"

class SongUpdateView(UpdateView):
	model = Song
	fields = ["name", "length"]
	success_url = "/"

class SongDeleteView(DeleteView):
	model = Song
	success_url = "/"

