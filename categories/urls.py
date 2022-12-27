from django.urls import path
from . import views

urlpatterns = [
    path("", views.Categories.as_view()),  # if we put a class name here we have to put as_view()
    path(
        "<int:pk>",
        views.CategoryDetail.as_view(),
    ),
]
