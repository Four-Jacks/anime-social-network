from django.urls import path, re_path
from .views import login_view, view_profile, edit_profile
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', view_profile),
    path('profile/', view_profile)

]
