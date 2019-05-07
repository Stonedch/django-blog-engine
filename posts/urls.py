from django.urls import path

from .views import *


urlpatterns = [
    path("", get_posts_list, name="posts_list_url"),
    path("post/<str:slug>/", get_post_detail, name="post_detail_url"),
    path("tag-list/", get_tag_list, name="tag_list_url"),
]