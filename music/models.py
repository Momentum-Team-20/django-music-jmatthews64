from django.db import models


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=255)
    number_of_tracks = models.IntegerField(blank=True, null=True)
    artist = models.ForeignKey(
        'Artist', on_delete=models.CASCADE,  related_name='albums'
    )
    # TODO add song list, add artist

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    # TODO add album list

    def __str__(self):
        return self.name


class Song():
    pass
