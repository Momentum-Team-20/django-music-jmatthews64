from django.forms import ModelForm
from .models import Album


class NewAlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'number_of_tracks')
