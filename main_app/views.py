from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Movie, Cast, Collection
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms

class Home(TemplateView):
    template_name = "home.html"

@method_decorator(login_required, name='dispatch')
class Collections(TemplateView):
    template_name = "collections.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_collections = Collection.objects.filter(user=self.request.user)
        context["collections"] = user_collections
        return context

@method_decorator(login_required, name='dispatch')
class MovieList(TemplateView):
    template_name = "movie_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["movies"] = Movie.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["movies"] = Movie.objects.filter(user=self.request.user)
            context["header"] = "Matt's Movie Database"
        return context


class MovieCreate(CreateView):
    model = Movie
    fields = ['name', 'image', 'release_date', 'synopsis', 'rating']
    template_name = "movie_create.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MovieCreate, self).form_valid(form)
    def get_success_url(self):
        print(self.kwargs)
        return reverse('movie_detail', kwargs={'pk': self.object.pk})


class MovieDetail(DetailView):
    model = Movie
    template_name = "movie_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collections'] = Collection.objects.all()
        return context

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

@method_decorator(login_required, name='dispatch')
class CollectionCastAssoc(View):
    def get(self, request, pk, cast_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Collection.objects.get(pk=pk).casts.remove(cast_pk)
        if assoc == "add":
            Collection.objects.get(pk=pk).casts.add(cast_pk)
        return redirect('collections')

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_list')
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class CollectionCreate(View):
    def get(self, request):
        form = CollectionForm()
        return render(request, 'create_collection.html', {'form': form})

    def post(self, request):
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.user = request.user 
            collection.save()
            return redirect('collections')
        return render(request, 'create_collection.html', {'form': form})

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['title']
