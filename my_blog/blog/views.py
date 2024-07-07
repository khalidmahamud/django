from datetime import date

from django.shortcuts import get_object_or_404, render

from .models import Post

all_posts = Post.objects.all().order_by("-date")

# Create your views here.


def home_page(request):
    latest_posts = all_posts[:3]
    return render(
        request,
        "blog/home.html",
        {
            "posts": latest_posts,
        },
    )


def posts_page(request):
    return render(
        request,
        "blog/posts.html",
        {
            "all_posts": all_posts,
        },
    )


def single_post_page(request, slug):
    identified_post = get_object_or_404(all_posts, slug=slug)
    return render(
        request,
        "blog/single_post.html",
        {
            "post": identified_post,
            "post_tags": identified_post.tags.all(),
        },
    )
