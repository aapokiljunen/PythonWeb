from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
	path('', BookListView.as_view()),
	path('book/<int:pk>', BookUpdateView.as_view()),
	path('book/new', BookCreateView.as_view()),
	path('book/<int:pk>/delete', BookDeleteView.as_view()),
	path('authorlist', AuthorListView.as_view()),
	path('author/<int:pk>', AuthorUpdateView.as_view()),
	path('author/new', AuthorCreateView.as_view()),
	path('author/<int:pk>/delete', AuthorDeleteView.as_view()),
	#path('author/<int:pk>/booklist', AuthorBookListView.as_view()),

	path('accounts/login/',LoginView.as_view(next_page="/")),
]
