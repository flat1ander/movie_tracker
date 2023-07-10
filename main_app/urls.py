from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('collections/', views.Collections.as_view(), name="collections"),
    path('movies/', views.MovieList.as_view(), name="movie_list"),
    path('movies/new/', views.MovieCreate.as_view(), name="movie_create"),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name="movie_detail"),
    path('movies/<int:pk>/update', views.MovieUpdate.as_view(), name="movie_update"),
    path('movies/<int:pk>/delete', views.MovieDelete.as_view(), name="movie_delete"),
    path('movies/<int:pk>/casts/new/', views.CastCreate.as_view(), name="cast_create"),
    path('collections/<int:pk>/casts/<int:cast_pk>/', views.CollectionCastAssoc.as_view(), name="collection_cast_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('collections/new/', views.CollectionCreate.as_view(), name="create_collection"),
]