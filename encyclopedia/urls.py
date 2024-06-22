from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("format_page", views.format_page, name="format_page"),
    path("random", views.random_entry, name="random_entry"),
    path("<str:title>", views.entry, name="entry")
]
