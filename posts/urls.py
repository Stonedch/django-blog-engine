from django.urls import path

from .views import *


urlpatterns = [
    path("", PostListView.as_view(), name="post_list_url"),
    path("post/<str:slug>/", PostDetailView.as_view(), name="post_detail_url"),
    path("post-create/", PostCreate.as_view(), name="post_create_url"),
    path("post-update/<str:slug>/", PostUpdate.as_view(), name="post_update_url"),
    path("tag-list/", TagListView.as_view(), name="tag_list_url"),
    path("tag/<str:slug>/", TagDetailView.as_view(), name="tag_detail_url"),
    path("tag-create/", TagCreate.as_view(), name="tag_create_url"),
    path("tag-update/<str:slug>/", TagUpdate.as_view(), name="tag_update_url"),
]