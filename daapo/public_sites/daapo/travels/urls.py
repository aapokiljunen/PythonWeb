from django.urls import path
from .views import *

urlpatterns = [
    path('', TripListView.as_view()),
    path('trip/new', TripCreateView.as_view()),
    path('trip/<int:pk>', TripUpdateView.as_view()),
    path('trip/<int:pk>/delete', TripDeleteView.as_view()),

    path('travellerlist', TravellerListView.as_view()),
    path('traveller/new', TravellerCreateView.as_view()),
    path('traveller/<int:pk>', TravellerUpdateView.as_view()),
    path('traveller/<int:pk>/delete', TravellerDeleteView.as_view()),
    
	path('destinationlist', DestinationListView.as_view()),
    path('destination/new', DestinationCreateView.as_view()),
    path('destination/<int:pk>', DestinationUpdateView.as_view()),
    path('destination/<int:pk>/delete', DestinationDeleteView.as_view()),
    
]
