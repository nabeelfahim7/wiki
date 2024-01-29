from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.page_render, name="page_render"),
    path("create", views.create, name="newpage")
    
]
