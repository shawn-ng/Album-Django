from django.shortcuts import render
from rest_framework import viewsets

from artists.models import Artist
from .serializers import ArtistSerializer, ArtistMemberSerializer
# Create your views here.
from .models import Artist, ArtistMember


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistMemberViewSet(viewsets.ModelViewSet):
    queryset = ArtistMember.objects.all()
    serializer_class = ArtistMemberSerializer
