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


# Cast Model Below:
class Cast(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="casts")
    def __str__(self):
        return self.name


# #Collection Model Below:
class Collection(models.Model):
    title = models.CharField(max_length=150)
    casts = models.ManyToManyField(Cast)
    def __str__(self):
        return self.title