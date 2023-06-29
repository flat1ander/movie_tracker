from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('streaming_playlist/', views.Streaming.as_view(), name="streaming_playlist"),
    path('movies/', views.MovieList.as_view(), name="movie_list"),
    path('movies/new/', views.MovieCreate.as_view(), name="movie_create"),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name="movie_detail"),
    path('movies/<int:pk>/update', views.MovieUpdate.as_view(), name="movie_update"),
    
]