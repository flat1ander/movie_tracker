from django.db import models

# Movie Model Below:
class Movie(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=1000)
    release_date = models.CharField(max_length=200)
    synopsis = models.CharField(max_length=5000)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# Streamer Model Below:

