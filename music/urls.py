from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_album, name='home'),
    path('artists/', views.list_artist, name='artists'),
    path('album/<int:pk>', views.album_details, name='album-details'),
    path('albums/new-album', views.create_new_album, name="new-album"),
    path('artists/new-artist', views.add_new_artist, name='new-artist'),
    path('album/<int:pk>/edit', views.edit_album, name='edit-album'),
    path('artist/<int:pk>', views.artist_details, name='artist-details'),
    path('album/<int:pk>/delete', views.delete_album, name='delete-album'),
]
