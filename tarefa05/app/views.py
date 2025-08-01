from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('data_pub')
    return render(request, 'app/index.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'app/post_detail.html', {'post': post})
