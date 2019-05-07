from django.shortcuts import render

from .models import *


def get_posts_list(request):
    posts = Post.objects.all()
    return render(request, "posts/posts-list.html", context={"posts": posts})


def get_post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post-detail.html", context={"post": post})


def get_tag_list(request):
    tags = Tag.objects.all()
    return render(request, "posts/tag-list.html", context={"tags": tags})


def get_tag_detail(request, slug):
    tag = Tag.objects.get(slug=slug)
    return render(request, "posts/tag-detail.html", context={"tag": tag})