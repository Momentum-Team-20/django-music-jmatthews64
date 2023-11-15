from django.forms import ModelForm
from .models import Album, Artist


class NewAlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'number_of_tracks')


class NewArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ('name',)


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'number_of_tracks')
