from django.shortcuts import render
from django.views import View
from accounts.models import UserAnime, UserFriend

# Create your views here.

#return render(request, 'posts.html')


class PostView(View):

    def get(self, request):
        try:
            friend = UserFriend.objects.get(current_user=request.user)
            friends = friend.friend.all()
        except UserFriend.DoesNotExist:
            friends = None

        user = request.user
        args = {'user': user, 'friends': friends}
        return render(request, 'posts.html', args)
