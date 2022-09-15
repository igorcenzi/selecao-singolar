from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostsView.as_view(), name="posts"),
    path("<str:id_post>/", views.PostRetrieveUpdateDestroyView.as_view(), name="posts"),
    path("all/", views.PostListAllView.as_view(), name="posts"),
]
