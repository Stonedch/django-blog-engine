from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import redirect_blog


urlpatterns = [
    path("", redirect_blog),
    path("admin/", admin.site.urls),
    path("post-list/", include("posts.urls"), name="post_list_url"),
]
