from django.shortcuts import render
from rest_framework import viewsets
from .models import Playlist, Song
from .serializers import PlaylistSerializer, SongSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer