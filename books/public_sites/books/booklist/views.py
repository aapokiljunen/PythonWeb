from django.views.generic import TemplateView, ListView
from .models import *

class BookListView(ListView):
	model = Book
