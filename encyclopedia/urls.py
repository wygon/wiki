from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newPage/", views.newPage, name="newPage"),
    path("search/", views.search, name="search"),
    path("randomPage/", views.randomPage, name="randomPage"),
    path("wiki/<str:title>/", views.wiki, name="wiki"),
    path("<str:title>/editPage", views.editPage, name="editPage")
]
