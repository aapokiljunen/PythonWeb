from django.urls import path
from .views import *

urlpatterns = [
	path('', SongListView.as_view()),
	path('song/new', SongCreateView.as_view()),
	path('song/<int:pk>', SongUpdateView.as_view()),
	path('song/<int:pk>/delete', SongDeleteView.as_view()),
]
