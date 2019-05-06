from django.shortcuts import render

from .models import Post


def get_posts_list(request):
    posts = Post.objects.all()
    return render(request, "posts/posts-list.html", context={"posts": posts})