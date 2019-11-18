from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from anime.models import Anime
from accounts.models import UserAnime, UserFriend

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
        next = request.GET.get('next')
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect('/')

        context = {
            'form': form,
        }
        return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/search')


def view_profile(request, pk=None):
    try:
        anime = UserAnime.objects.get(current_anime=request.user)
        animes = anime.anime.all()
    except UserAnime.DoesNotExist:
        animes = None

    try:
        friend = UserFriend.objects.get(current_user=request.user)
        friends = friend.friend.all()
    except UserFriend.DoesNotExist:
        friends = None

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user, 'animes': animes, 'friends': friends}
    return render(request, 'profile.html', args)


def change_anime(request, operation, pk):
    new_anime = Anime.objects.get(pk=pk)
    if operation == 'add':
        UserAnime.add_anime(request.user, new_anime)
    elif operation == 'remove':
        UserAnime.remove_anime(request.user, new_anime)
    return redirect('/')


def change_friend(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        UserAnime.add_anime(request.user, new_friend)
    elif operation == 'remove':
        UserAnime.remove_anime(request.user, new_friend)
    return redirect('/')


def view_friend(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'friend.html', args)
