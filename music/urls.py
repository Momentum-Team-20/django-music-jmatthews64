from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_album, name='home'),
    path('artists/', views.list_artist, name='artists'),
    path('album/<int:pk>', views.album_details, name='album-details'),
    path('albums/new-album', views.create_new_album, name="new-album"),
    path('artists/new-artist', views.add_new_artist, name='new-artist'),
]
