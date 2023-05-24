from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import *

class BookListView(ListView):
	model = Book

class BookUpdateView(UpdateView):
	model = Book
	fields = ["name", "review"]
	success_url = "/"

class BookCreateView(CreateView):
	model = Book
	fields = ["name", "review"]
	success_url = "/"

class BookDeleteView(DeleteView):
	model = Book
	success_url = "/"
