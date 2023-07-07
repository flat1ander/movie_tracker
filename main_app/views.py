from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Movie, Cast, Collection
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect

class Home(TemplateView):
    template_name = "home.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["collections"] = Collections.objects.all()
    #     return context

class Collections(TemplateView):
    template_name = "collections.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collections"] = Collection.objects.all()
        return context


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
    def get_success_url(self):
        return reverse('movie_detail', kwargs={'pk': self.object.pk})


class MovieDetail(DetailView):
    model = Movie
    template_name = "movie_detail.html"

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['name', 'image', 'release_date', 'synopsis', 'rating']
    template_name = "movie_update.html"
    def get_success_url(self):
        return reverse('movie_detail', kwargs={'pk': self.object.pk})

class MovieDelete(DeleteView):
    model = Movie
    template_name = "movie_delete.html"
    success_url = "/movies/"

class CastCreate(View):
    def post (self, request, pk):
        name = request.POST.get("name")
        role = request.POST.get("role")
        movie = Movie.objects.get(pk=pk)
        Cast.objects.create(name=name, role=role, movie=movie)
        return redirect('movie_detail', pk=pk)

