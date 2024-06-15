from django.urls import path

from . import views


urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("posts", views.posts_page, name="posts-page"),
    path(
        "paths/<slug:slug>", views.single_post_page, name="single-posts-page"
    ),  # posts/my-first-post
]
