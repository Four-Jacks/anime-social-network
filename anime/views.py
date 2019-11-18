from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q
from .models import Anime
from anime.forms import AnimeForm


class AnimeView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        query = 'Fall 2019'
        object_list = Anime.objects.filter(
            Q(season__icontains=query)
        )
        return object_list


class SearchResultsView(ListView):
    model = Anime
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Anime.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


class AnimeDetailView(DetailView):
    template_name = 'anime_detail.html'
    queryset = Anime.objects.all()
