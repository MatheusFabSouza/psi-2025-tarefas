from django.shortcuts import render, get_object_or_404
from .models import Post, Blog

def index(request):
    context = {
        "posts": Post.objects.all(),
        "blog": Blog.objects.first(),
    }
    return render(request, "app/index.html", context)

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'app/post_detail.html', {'post': post})
