from django.urls import path  
from .views import HomePageView, AboutPageView, PostsPageView, CreatePageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("create/", CreatePageView.as_view(), name='create'),
    # path("posts/", PostsPageView.as_view(), name='posts'),
]