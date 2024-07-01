from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import Avg

from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating", "title")
    total_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))

    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_books": total_books,
            "avg_rating": avg_rating
        },
    )


def book_detail(request, id, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, pk=id)
    if slug != book.slug:
        raise Http404()

    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_best_selling": book.is_best_selling,
        },
    )


def book_detail_id(request, id):
    book = get_object_or_404(Book, pk=id)
    slug = slugify(book.title)
    redirect_path = reverse("book-detail", kwargs={"id": id, "slug": slug})
    return HttpResponseRedirect(redirect_path)
