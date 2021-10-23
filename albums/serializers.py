from rest_framework import serializers
from .models import Albums

# converting data from json into the necesarrily format


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        # model that the serializer is based on
        model = Albums
        # fields that include in the serialization
        fields = "__all__"
        # / fields = ['artist', 'title', 'cover_image', 'id']-> this is another way of writing.
