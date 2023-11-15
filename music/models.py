from django.db import models


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(
        'Artist', on_delete=models.CASCADE,  related_name='albums'
    )
    number_of_tracks = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # TODO add song list

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # TODO add album list

    def __str__(self):
        return self.name


class Song():
    pass
