from django.contrib.auth.models import User
from django.db import models

# Genre choices for movies
GENRE_CHOICES = (
    ('Action', 'Action'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    # Add other genre choices as needed
)


class Movie(models.Model):
    series_title = models.CharField(max_length=100)
    overview = models.TextField(max_length=1000)
    poster_link = models.URLField(max_length=250, null=True, blank=True)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=10)
    imdb_rating = models.IntegerField()
    runtime = models.IntegerField(default=0)
    star1 = models.CharField(max_length=100)
    star2 = models.CharField(max_length=100)
    star3 = models.CharField(max_length=100)
    released_year = models.IntegerField(default=0)
    gross = models.IntegerField(default=0)
    director = models.CharField(default='', max_length=100)
    users = models.ManyToManyField(User, related_name='watched_movies')

    def __str__(self):
        return self.series_title


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        unique_together = ('user', 'movie')


class Quotes(models.Model):
    quote = models.CharField(max_length=100)
    by = models.CharField(max_length=100)
