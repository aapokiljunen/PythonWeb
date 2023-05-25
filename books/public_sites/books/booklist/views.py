from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

class BookListView(LoginRequiredMixin, ListView):
	model = Book

class BookUpdateView(LoginRequiredMixin, UpdateView):
	model = Book
	fields = ["name", "author", "review"]
	success_url = "/"

class BookCreateView(LoginRequiredMixin, CreateView):
	model = Book
	fields = ["name", "author",  "review"]
	success_url = "/"

class BookDeleteView(LoginRequiredMixin, DeleteView):
	model = Book
	success_url = "/"

class AuthorListView(LoginRequiredMixin, ListView):
	model = Author

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
	model = Author
	fields = ["first_name", "last_name"]
	success_url = "/"

class AuthorCreateView(LoginRequiredMixin, CreateView):
	model = Author
	fields = ["first_name", "last_name"]
	success_url = "/"

class AuthorDeleteView(LoginRequiredMixin, DeleteView):
	model = Author
	success_url = "/"

#class AuthorBookListView(ListView):
#	model = Book
