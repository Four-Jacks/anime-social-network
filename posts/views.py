from django.shortcuts import render
from django.views import View

# Create your views here.

#return render(request, 'posts.html')


class PostView(View):

    def get(self, request):
        return render(request, 'posts.html')
