from django.db import models

from artists.models import Artist

# Create your models here.


class Albums(models.Model):
    title = models.CharField(max_length=50)
    # you can store those stastic image in a static server.
    cover_image = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.
                               CASCADE, default=None, null=True)

    def __str__(self):
        return f'{self.title} by {self.artist} ({self.id})'
