from .models import Playlist
from rest_framework import serializers

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist 
        fields = ['id', 'name', 'song1', 'song2', 'song3', 'song4']