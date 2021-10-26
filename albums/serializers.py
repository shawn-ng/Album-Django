from rest_framework import serializers
from .models import Albums

# converting data from json into the necesarrily format

# hyperlink serializer -> the other model that link to it able to portray the info better


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        # model that the serializer is based on
        model = Albums
        # fields that include in the serialization
        fields = "__all__"
        # / fields = ['artist', 'title', 'cover_image', 'id']-> this is another way of writing.
        depth = 2
