from django.urls import path
from .views import AlbumDetailView, index, AlbumListView

urlpatterns = [
    path('', index),
    # calling the class from view
    path('api/', AlbumListView.as_view()),
    path('api/<int:id>', AlbumDetailView.as_view())
]
