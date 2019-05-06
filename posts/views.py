from django.shortcuts import render

from .models import Post


def get_posts_list(request):
    posts = Post.objects.all()
    return render(request, "posts/posts-list.html", context={"posts": posts})

def get_post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post-detail.html", context={"post": post})