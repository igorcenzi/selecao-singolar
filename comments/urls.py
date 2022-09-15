from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommentsCreateListView.as_view()),
    path('<str:post_id>/', views.PostCommentsListView.as_view()),
    path('id/<str:comment_id>/', views.CommentRetrieveUpdateDestroyView.as_view()),
]
