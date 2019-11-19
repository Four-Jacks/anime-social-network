from django.shortcuts import render
from django.views import View
from accounts.models import User

# Create your views here.

#return render(request, 'posts.html')


class PostView(View):

    def get(self, request):
        #query = self.request.GET.get('q')
        users = User.objects.all().order_by('username')

        args = {'users': users}
        return render(request, 'posts.html', args)
