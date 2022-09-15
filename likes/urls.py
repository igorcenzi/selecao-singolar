from django.urls import path
from . import views

urlpatterns = [
    path('', views.LikeCreateView.as_view()),
    path('comment/<str:id_comment>/', views.ListCommentLikesView.as_view()),
    path('<str:id_comment>/', views.LikeDestroyView.as_view()),
]
