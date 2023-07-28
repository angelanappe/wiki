from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newpage, name="new_page"),
    path("editpage/", views.editpage, name="edit"),
    path("edited/", views.edited, name="edited"),
    path("random_function/", views.random_function, name="random_function")
]
