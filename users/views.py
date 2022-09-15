from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import generics
# Create your views here.
class CreateUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class RetrieveUpdateDestroyUserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"
    lookup_field = "id"