from django.urls import path
from posts import views

urlpatterns = [
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path("", views.PostListView.as_view(), name="posts"),
    path("new/", views.PostCreateView.as_view(), name="new"),
    path("<int:pk>/detail/", views.PostDetailView.as_view(), name="post_detail"),
]