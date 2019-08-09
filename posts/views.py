from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import *
from .models import *
from .forms import *


class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "posts/post-list.html", context={"posts": posts})


class PostDetailView(ObjectDetailMixin, View):
    model = Post
    template = "posts/post-detail.html"


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    raise_exception = True
    form_model = PostForm
    template = "posts/post-create.html"


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    raise_exception = True
    model = Post
    form_model = PostForm
    template = "posts/post-update.html"


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    raise_exception = True
    model = Post
    template = "posts/post-delete.html"
    reverse_url = "post_list_url"


class TagListView(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, "posts/tag-list.html", context={"tags": tags})


class TagDetailView(LoginRequiredMixin, ObjectDetailMixin, View):
    raise_exception = True
    model = Tag
    template = "posts/tag-detail.html"


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    raise_exception = True
    form_model = TagForm
    template = "posts/tag-create.html"


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    raise_exception = True
    model = Tag
    form_model = TagForm
    template = "posts/tag-update.html"


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    raise_exception = True
    model = Tag
    template = "posts/tag-delete.html"
    reverse_url = "tag_list_url"