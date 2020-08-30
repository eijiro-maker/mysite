from django.shortcuts import render
from django.views import generic
from .models import Movie
from django.db.models import Q
from moviedb.forms import SearchForm
from django.utils import timezone

# Create your views here.

class IndexView(generic.ListView):
    model = Movie
    template_name = "moviedb/index.html"
    paginate_by = 10
    f = SearchForm()

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Movie.objects.filter(
                Q(title__icontains=q_word) | Q(explain__icontains=q_word))
        else:
            object_list = Movie.objects.all()
        RNum = object_list.count
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['Qstring'] = self.request.GET.get('query')
        context['qword'] = self.request.GET.urlencode()
        context['Num'] = self.object_list.count()
        return context

class MovieDetail(generic.DetailView):
    model = Movie

class Movielist(generic.ListView):
    model = Movie
    template_name = 'moviedb/movie_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        #return qs.filter(explain__startswith=self.kwargs['name'])
        return qs.filter(explain__icontains='アカデミー')