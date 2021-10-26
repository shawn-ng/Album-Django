from rest_framework import serializers
from .models import Artist, ArtistMember
from albums.serializers import AlbumShallowSerializer


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    albums = AlbumShallowSerializer(many=True, read_only=True)
    print(albums)

    class Meta:
        # model that the serializer is based on
        model = Artist
        # fields that include in the serialization
        fields = (
            "id", "name", "members", "albums")

        depth = 2


class ArtistMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model that the serializer is based on
        model = ArtistMember
        # fields that include in the serialization
        fields = ("id", "name", "date_of_birth", "artists")

        depth = 1
