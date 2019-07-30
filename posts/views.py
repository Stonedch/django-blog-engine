from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .utils import ObjectDetailMixin, ObjectCreateMixin
from .models import *
from .forms import *


class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "posts/post-list.html", context={"posts": posts})


class PostDetailView(ObjectDetailMixin, View):
    model = Post
    template = "posts/post-detail.html"


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = "posts/post-create.html"

class TagListView(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, "posts/tag-list.html", context={"tags": tags})


class TagDetailView(ObjectDetailMixin, View):
    model = Tag
    template = "posts/tag-detail.html"


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = "posts/tag-create.html"