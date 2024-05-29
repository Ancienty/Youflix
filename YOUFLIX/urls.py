"""
URL configuration for YOUFLIX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from account import views
from movie.views import home, movie_list, stats
from account.views import profile, add_to_watchlist

urlpatterns = [
    path('stats/', stats, name='stats'),
    path('profile/', profile, name='profile'),
    path('movies/', movie_list, name='movie-list'),
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('register/',views.user_register,name="user_register"),
    path('logout/',views.user_logout,name="user_logout"),
    path('add_to_watchlist/', add_to_watchlist, name='add_to_watchlist'),
    path('remove_from_watchlist/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('rate_movie/', views.rate_movie, name='rate_movie'),
    path('', home, name='home'),

]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
