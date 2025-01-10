from django.urls import path
from .views import HomeView

from .views import trip_list, TripCreateView, NoteListView, TripDetail, NoteDetail, NoteUpdateView, NoteDeleteView
from .views import NoteCreateView, TripUpdateView, TripDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', trip_list, name= 'trip-list'),
    path('dashboard/note/', NoteListView.as_view(), name= 'note-list'),
    path('dashboard/note/create/', NoteCreateView.as_view(), name='note-create'),
    path('dashboard/trip/create/', TripCreateView.as_view(), name='trip-create'),
    path('dashboard/trip/<int:pk>/', TripDetail, name='trip-detail'),
    path('dashboard/note/<int:pk>/', NoteDetail, name='note-detail'),
    path('dashboard/note/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('dashboard/note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('dashboard/trip/<int:pk>/update/', TripUpdateView.as_view(), name='trip-update'),
    path('dashboard/trip/<int:pk>/delete/', TripDeleteView.as_view(), name='trip-delete'),


]
