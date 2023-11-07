from django.db import models

# Create your models here.
#equivelent to models/schema in Mongoose 

class Playlist(models.Model):
    name = models.CharField(max_length=100) 
    song1 = models.CharField(max_length=100) 
    song2 = models.CharField(max_length=100) 
    song3 = models.CharField(max_length=100) 
    song4 = models.CharField(max_length=100) 