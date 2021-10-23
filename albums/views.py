from django.shortcuts import render

# rest framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions, status

# serializer
from albums.serializers import AlbumSerializer

# importing schema model
from .models import Albums

# Create your views here.


def index(request):

    # grabbing what we need from data base
    list = Albums.objects.all()
    # creating a context
    context = {"albums": list}
    # we are rendering on a template
    return render(request, 'albums/index.html', context)


class AlbumListView (APIView):

    # django rest framework make you dont need to put condition on whether your request is post or get or put
    def get(self, request):
        albums = Albums.objects.all()
        serelized_albums = AlbumSerializer(albums, many=True)
        return Response(serelized_albums.data, status=status.HTTP_200_OK)

    def post(self, request):
        album_added = AlbumSerializer(data=request.data)
        # checking for validatity
        if album_added.is_valid():
            # save the album to database
            album_added.save()
            # return a response
            return Response(album_added.data, status=status.HTTP_201_CREATED)

        return Response(album_added.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetailView (APIView):
    def get_show_by_id(self, id):
        # checking for whether album exist
        try:
            album = Albums.objects.get(id=id)
            return album
        except Albums.DoesNotExist:
            raise exceptions.NotFound(detail="Album not found")

    # getting single album
    def get(self, request, id):
        album = self.get_show_by_id(id)
        # serialization
        serelized_album = AlbumSerializer(album, many=False)
        # response
        return Response(serelized_album.data, status=status.HTTP_200_OK)

    # deleteing single album
    def delete(self, request, id):
        album = self.get_show_by_id(id)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # updating
    def put(self, request, id):
        album = self.get_show_by_id(id)
        updated_album = AlbumSerializer(album, data=request.data)
        if updated_album.is_valid():
            updated_album.save()
            return Response(updated_album.data, status=status.HTTP_202_ACCEPTED)

        return Response(updated_album._errors, status=status.HTTP_400_BAD_REQUEST)
