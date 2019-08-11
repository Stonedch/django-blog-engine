from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

from .utils import *
from .models import *
from .forms import *


class PostListView(View):
    def get(self, request):
        page_number = request.GET.get("page", 1)
        search_query = request.GET.get("search", "")

        if search_query:
            posts = Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
        else:
            posts = Post.objects.all()

        paginator = Paginator(posts, 2)
        page = paginator.get_page(page_number)
        previous_page_url = next_page_url = "?page={}".format(page.number)

        if page.has_previous():
            previous_page_url = "?page={}".format(page.previous_page_number())
        if page.has_next():
            next_page_url = "?page={}".format(page.next_page_number())

        context = {
            "page": page,
            "next_page_url": next_page_url,
            "previous_page_url": previous_page_url
        }

        return render(request, "posts/post-list.html", context)


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