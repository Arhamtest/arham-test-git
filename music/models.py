from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist + ' - ' + self.genre


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField()
    is_favorite = models.BooleanField(default=False)
    song_price = models.CharField(max_length=15, default='')
    song_number = models.CharField(max_length=10 , default='')
    song_desc = models.TextField(max_length=500, default='')

    def __str__(self):
        return self.song_title + ' - ' + self.song_number
