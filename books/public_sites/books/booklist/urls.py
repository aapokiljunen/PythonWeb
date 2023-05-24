from django.urls import path
from .views import *

urlpatterns = [
	path('', BookListView.as_view()),
	path('book/<int:pk>', BookUpdateView.as_view()),
	path('book/new', BookCreateView.as_view()),
	path('book/<int:pk>/delete', BookDeleteView.as_view()),
]
