from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import YES
from django.db import models

# Create your models here.
class Artiste (models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age= models.IntegerField(max_lenght=3)

class Song (models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateField(max_length=10)
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Lyrics (models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

