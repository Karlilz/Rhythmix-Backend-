from rest_framework import generics
from .models import Playlist
from .serializers import PlaylistSerializer

class PLaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get (self, request, *args, **kwargs):
        queryset = Playlist.objects.get(owner=request.user)
        serializer = PlaylistSerializer(queryset, many=True)
        return self.list(request, *args, **kwargs)

class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer