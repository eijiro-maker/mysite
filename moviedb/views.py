from django.shortcuts import render
from django.views import generic
from .models import Movie
from django.db.models import Q

# Create your views here.

class IndexView(generic.ListView):
    model = Movie
    template_name = "moviedb/index.html"
    paginate_by = 10

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Movie.objects.filter(
                Q(title__icontains=q_word) | Q(explain__icontains=q_word))
        else:
            object_list = Movie.objects.all()
        return object_list

class MovieDetail(generic.DetailView):
    model = Movie

class Movielist(generic.ListView):
    model = Movie
    template_name = 'moviedb/index.html'
    paginate_by = 10
