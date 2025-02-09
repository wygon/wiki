from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newPage/", views.newPage, name="newPage"),
    path("search/", views.search, name="search"),
    path("randomPage/", views.randomPage, name="randomPage"),
    path("<str:title>/", views.page, name="page"),
    path("<str:title>/editPage", views.editPage, name="editPage")
]
