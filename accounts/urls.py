from django.urls import path, re_path
from .views import login_view, view_profile
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login', login_view),
    path('profile/', view_profile),
    #path('profile/<username>/', view_profile, name='view_profile_with_username')

]
