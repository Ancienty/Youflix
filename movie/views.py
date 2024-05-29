from collections import Counter, defaultdict

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from .models import Movie, Quotes, Rating
import random
import json


def movie_list(request):
    all_movies = list(Movie.objects.all())
    movies = random.sample(all_movies, min(30, len(all_movies)))
    initial_movie_data = json.dumps([{'poster_link': movie.poster_link, 'series_title': movie.series_title} for movie in movies])
    add_to_watchlist_url = reverse('add_to_watchlist')
    context = {
        'movies': movies,
        'initial_movie_data': initial_movie_data,
        'add_to_watchlist_url': add_to_watchlist_url
    }
    return render(request, 'movie/movies.html', context)


def home(request):
    all_quotes = list(Quotes.objects.all())
    quotes = random.choice(all_quotes)
    initial_quote_data = [
        {'quote': quotes.quote, 'by': quotes.by}
    ]

    highest_rating = Movie.objects.order_by('-imdb_rating').values_list('imdb_rating', flat=True).first()
    top_rated_movies = Movie.objects.order_by('-imdb_rating')[:5]
    context = {
        'quotes': quotes,
        'initial_quote_data': initial_quote_data,
        'top_rated_movies': top_rated_movies,
    }

    return render(request, 'movie/home.html', context)


@login_required
def stats(request):
    user = request.user
    watched_movies = user.profile.watched_movies.all()
    total_movies_watched = watched_movies.count()

    # Calculate total minutes watched by summing the runtime of each watched movie
    total_minutes_watched = sum(int(movie.runtime.split(" min")[0]) for movie in watched_movies)

    # Get all the ratings given by the user
    ratings = Rating.objects.filter(user=user)

    # Calculate the favorite genre based on distributed ratings
    genre_ratings = Counter()
    actor_ratings = Counter()

    for rating in ratings:
        genres = rating.movie.genre.split(',')  # Assuming genres are comma-separated
        for genre in genres:
            genre_ratings[genre.strip()] += rating.rating  # Strip to remove any leading/trailing spaces
        # Count actors only from rated movies
        actors = [rating.movie.star1, rating.movie.star2, rating.movie.star3]
        for actor in actors:
            actor_ratings[actor.strip()] += rating.rating

    # Get the top 3 genres by total rating
    top_genres = genre_ratings.most_common(3)

    # Get the top 3 actors by total rating
    favorite_actors = actor_ratings.most_common(3)

    # Get top 5 highest rated movies
    top_rated_movies = ratings.order_by('-rating')[:5]

    context = {
        'total_movies_watched': total_movies_watched,
        'total_minutes_watched': total_minutes_watched,
        'top_genres': top_genres,
        'favorite_actors': favorite_actors,
        'top_rated_movies': top_rated_movies
    }

    return render(request, 'movie/stats.html', context)
