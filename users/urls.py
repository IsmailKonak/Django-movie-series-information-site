from django.urls import path
from users import views as users_views
from main import views as main_views
from main.models import Movie, Series, Categorie
from slugify import slugify
    

urlpatterns = [
    path('login', users_views.login, name="login"),
    path('register', users_views.register, name="register"),
    path('logout', users_views.logout_view, name="logout"),
    path('profile/<str:username>',main_views.profile, name="profile"),
    path('',main_views.home, name="home"),
    path('series',main_views.series, name="series"),
    path('movies',main_views.movies, name="movies"),
    path('search',main_views.search, name="search"),
    path('addcontent',main_views.addcontent, name="addcontent"),
]
for movie in Movie.objects.all():
    urlpatterns.append(path(('movies/'+str(movie.url_name)),main_views.movies,{"movie_name":movie.name}, name="movies"))

for series in Series.objects.all():
    urlpatterns.append(path(('series/'+str(series.url_name)),main_views.series,{"series_name":series.name}, name="series"))

for category in Categorie.objects.all():
    urlpatterns.append(path((f'search/category="{category.category}"'),main_views.search,{"categorie":category.category,"query":"category="+category.category}, name="category"))


