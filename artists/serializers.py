from rest_framework import serializers
from .models import Artist, ArtistMember


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model that the serializer is based on
        model = Artist
        # fields that include in the serialization
        fields = "__all__"
        # / fields = ['artist', 'title', 'cover_image', 'id']-> this is another way of writing.
        depth = 2


class ArtistMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model that the serializer is based on
        model = ArtistMember
        # fields that include in the serialization
        fields = "__all__"
        # / fields = ['artist', 'title', 'cover_image', 'id']-> this is another way of writing.
