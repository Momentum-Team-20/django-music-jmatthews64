from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_album, name='home'),
    path('artists/', views.list_artist, name='artists'),
    path('album/<int:pk>', views.album_details, name='album-details'),
    path('album/<int:coll_pk>/new', views.create_new_album, name="new-album"),
]
