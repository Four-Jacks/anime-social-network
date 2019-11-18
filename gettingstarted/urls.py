from django.contrib import admin
from django.urls import path, include, re_path
from accounts.views import login_view, logout_view, register_view, view_profile, change_anime, change_friend
from django.contrib.auth import views as auth_views

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view),
    path('profile/', view_profile),
    path('search/', include('anime.urls')),
    path('posts/', include('posts.urls')),
    path('', include('anime.urls')),
    path('logout/', auth_views.LogoutView.as_view()),

    re_path(r'update/(?P<operation>.+)/(?P<pk>\d+)', change_anime, name='change_anime'),
    re_path(r'connect/(?P<operation>.+)/(?P<pk>\d+)', change_friend, name='change_friend')
]
