from django.urls import path, include
from .views import AnimeView, SearchResultsView

app_name = 'anime'

urlpatterns = [
    path('results/', SearchResultsView.as_view(), name='search_results'),
    path('', AnimeView.as_view(), name='anime'),
]
