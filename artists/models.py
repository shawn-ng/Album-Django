from django.db import models


# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=50, default=None)
    members = models.ManyToManyField(
        to='ArtistMember', related_name='artists', blank=True)

    def __str__(self):
        return self.name


class ArtistMember(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(max_length=50)

    def __str__(self):
        return self.name
