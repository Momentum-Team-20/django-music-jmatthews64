from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Artist


# Create your views here.
def list_album(request):
    albums = Album.objects.all()
    return render(request, 'index.html', {'albums': albums})
