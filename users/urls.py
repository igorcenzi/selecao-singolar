from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateUserView.as_view()),
    path("<str:user_id>/", views.RetrieveUpdateDestroyUserDetailsView.as_view()),  
]