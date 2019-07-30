from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .utils import ObjectDetailMixin
from .models import *
from .forms import *


class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "posts/post-list.html", context={"posts": posts})


class PostDetailView(ObjectDetailMixin, View):
    model = Post
    template = "posts/post-detail.html"


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, "posts/post-create.html", context={"form": form})
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post)
        return render(request, "posts/post-create.html", context={"form": form})


class TagListView(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, "posts/tag-list.html", context={"tags": tags})


class TagDetailView(ObjectDetailMixin, View):
    model = Tag
    template = "posts/tag-detail.html"


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, "posts/tag-create.html", context={"form": form})
    
    def post(self, request):
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save()
            return redirect(tag)
        return render(request, "posts/tag-create.html", context={"form": form})