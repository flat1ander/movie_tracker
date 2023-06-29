from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Movie
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

class Home(TemplateView):
    template_name = "home.html"


class About (TemplateView):
    template_name = "about.html"


class MovieList(TemplateView):
    template_name = "movie_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = Movie.objects.all()
        return context


class MovieCreate(CreateView):
    model = Movie
    fields = ['name', 'image', 'release_date', 'synopsis', 'rating']
    template_name = "movie_create.html"
    success_url = "/movies/"


class MovieDetail(DetailView):
    model = Movie
    template_name = "movie_detail.html"