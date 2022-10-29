from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import YES
from django.db import models

# Create your models here.
class Artiste (models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.CharField(max_lenght=3)

class Song (models.Model):
    title=("Fire on the mountain")
    date_released= 2007
    likes = YES
    artiste_id = ("Asa")

class Lyrics (models.Model):
    content = ("")
    song_id = ("")
