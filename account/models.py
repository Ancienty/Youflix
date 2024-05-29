from django.contrib.auth.models import User
from django.db import models
from movie.models import Movie


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    watched_movies = models.ManyToManyField(Movie, blank=True)

    def __str__(self):
        return self.user.username
