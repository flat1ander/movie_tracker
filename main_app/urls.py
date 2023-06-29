from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('movies/', views.MovieList.as_view(), name="movie_list"),
    path('movies/new/', views.MovieCreate.as_view(), name="movie_create"),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name="movie_detail")
]