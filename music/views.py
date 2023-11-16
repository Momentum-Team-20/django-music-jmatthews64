from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewAlbumForm, NewArtistForm, AlbumForm
from .models import Album, Artist


# Create your views here.
def list_album(request):
    albums = Album.objects.all()
    return render(request, 'index.html', {'albums': albums})


def list_artist(request):
    artists = Artist.objects.all()
    return render(request, 'artist.html', {'artists': artists})


def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(
        request,
        'album_details.html',
        {'album': album}
    )


def artist_details(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'artist_details.html', {'artist': artist})


def create_new_album(request):
    album = Album.objects.all()
    if request.method == 'POST':
        form = NewAlbumForm(request.POST)
        new_album = form.save(commit=False)
        new_album.album = album
        new_album.save()
        return redirect('home')
    form = NewAlbumForm()
    return render(request, "new_album.html", {'form': form})


def add_new_artist(request):
    artist = Artist.objects.all()
    if request.method == 'POST':
        form = NewArtistForm(request.POST)
        new_artist = form.save(commit=False)
        new_artist.artist = artist
        new_artist.save()
        return redirect('artists')
    form = NewArtistForm()
    return render(request, "new_artist.html", {'form': form})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('album-details', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'edit_album.html', {'form': form})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.delete()
            return redirect('home',)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'delete_album.html', {'form': form})
