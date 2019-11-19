"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from accounts.views import (login_view,
                            logout_view,
                            register_view,
                            view_profile,
                            change_anime,
                            change_friend,
                            view_friend,
                            edit_profile)

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view),
    path('profile/', include('accounts.urls')),
    path('search/', include('anime.urls')),
    path('posts/', include('posts.urls')),
    path('', include('anime.urls')),
    path('logout/',auth_views.LogoutView.as_view()),
    path('edit/',edit_profile),

    path('profile/<int:pk>/', view_friend, name='friend_view'),

    re_path(r'update/(?P<operation>.+)/(?P<pk>\d+)', change_anime, name='change_anime'),
    re_path(r'connect/(?P<operation>.+)/(?P<pk>\d+)', change_friend, name='change_friend')
]
