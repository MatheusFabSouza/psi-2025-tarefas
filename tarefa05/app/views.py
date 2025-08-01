from django.shortcuts import render
from .models import Post, Blog

def index(request):
    context = {
        "posts": Post.objects.all(),
        "blog": Blog.objects.first(),
    }
    return render(request, "app/index.html", context)

def post_detail(request, id):
    return render(request, 'app/post_detail.html')

