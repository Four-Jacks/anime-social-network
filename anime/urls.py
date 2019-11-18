from django.urls import path, include
from .views import AnimeView, SearchResultsView, AnimeDetailView

app_name = 'anime'

urlpatterns = [
    path('results/', SearchResultsView.as_view(), name='search_results'),
    path('anime/<int:pk>/', AnimeDetailView.as_view(), name='anime_detail'),
    path('', AnimeView.as_view(), name='anime'),
]
