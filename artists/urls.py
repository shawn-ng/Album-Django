from django.urls import path, include
from rest_framework import routers

from .views import ArtistViewSet, ArtistMemberViewSet

router = routers.DefaultRouter()
router.register("artists", ArtistViewSet)
router.register("ArtistMember", ArtistMemberViewSet)

urlpatterns = [
    path("", include(router.urls))
]
