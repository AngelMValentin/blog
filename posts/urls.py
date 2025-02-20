from django.urls import path
from posts import views

urlspatterns = [
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.PostUpdateView.as_view(), name="delete"),
]