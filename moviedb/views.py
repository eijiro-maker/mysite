from django.shortcuts import render
from django.views import generic
from .models import Movie

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "moviedb/index.html"

class MovieDetail(generic.DetailView):
    model = Movie

class Movielist(generic.ListView):
    model = Movie
