from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, "blog/home.html")


def posts_page(request):
    return render(request, "blog/posts.html")


def single_post_page(request):
    pass
