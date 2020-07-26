from django.urls import path
from . import views

app_name = 'moviedb'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('detail/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'),
    path('list/', views.Movielist.as_view(), name='movie_list'),
]