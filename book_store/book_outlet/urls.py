from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>/", views.book_detail_id, name="book-detail-id"),
    path("<int:id>/<slug:slug>", views.book_detail, name="book-detail"),
]
