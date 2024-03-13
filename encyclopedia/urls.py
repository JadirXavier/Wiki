from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page>", views.entry_page, name="page"),
    path("search", views.search_page, name="search"),
    path("new", views.new_page, name="new"),
    path("wiki/<str:page>/edit/", views.edit_page, name="edit"),
    path("random", views.random_page, name="random"),
]
