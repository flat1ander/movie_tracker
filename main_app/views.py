from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Movie

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


