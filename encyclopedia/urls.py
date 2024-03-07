from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page>", views.entry_page, name="page"),
    path("search", views.search_page, name="search"),
    path("new_page", views.create_new_page, name="new_page")
]
