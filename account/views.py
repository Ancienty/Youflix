# account/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import json

from account.models import Profile
from movie.models import Movie, Rating

def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {"error": "Invalid username or password"})
    else:
        return render(request, "account/login.html")

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/register.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(request, "account/register.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("home")

@login_required(login_url='login')
def profile(request):
    user = request.user
    watched_movies = user.profile.watched_movies.all()
    ratings = Rating.objects.filter(user=request.user)
    movie_ratings = {rating.movie.id: rating.rating for rating in ratings}

    return render(request, 'account/profile.html', {'watched_movies': watched_movies, 'ratings': movie_ratings})

@login_required(login_url='login')
@csrf_exempt
def add_to_watchlist(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            movie_id = data.get('movie_id')
            movie = get_object_or_404(Movie, pk=movie_id)

            if not hasattr(request.user, 'profile'):
                Profile.objects.create(user=request.user)

            request.user.profile.watched_movies.add(movie)
            return JsonResponse({'status': 'success'})
        except Movie.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Movie not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
@login_required(login_url='login')
def remove_from_watchlist(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            movie_id = data.get('movie_id')
            movie = Movie.objects.get(id=movie_id)

            request.user.profile.watched_movies.remove(movie)
            Rating.objects.filter(user=request.user, movie=movie).delete()

            return JsonResponse({'status': 'success'})
        except Movie.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Movie not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
@login_required(login_url='login')
def rate_movie(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        movie_id = data.get('movie_id')
        rating_value = data.get('rating')

        try:
            movie = Movie.objects.get(id=movie_id)
            try:
                rating = Rating.objects.get(user=request.user, movie=movie)
                rating.rating = rating_value
            except Rating.DoesNotExist:
                rating = Rating(user=request.user, movie=movie, rating=rating_value)

            rating.save()
            return JsonResponse({'status': 'success'})
        except Movie.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Movie not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
