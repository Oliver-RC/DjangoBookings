from django.shortcuts import render
from blog.models import Post


blogs = Post.objects.all()


def index(request):
    context = {'blogs': blogs, }

    return render(request, 'index.html', context)
