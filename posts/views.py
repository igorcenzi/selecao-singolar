from rest_framework import generics
from .serializers import PostSerializer, PostWithCommentsSerializer
from .models import Posts
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from selecao_singolar.permissions import HasUserPermissions

# Create your views here.
class PostsView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
     serializer.save(user=self.request.user)
     
    def get_queryset(self):
       return Posts.objects.filter(user=self.request.user)
   
class PostListAllView(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
        
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasUserPermissions]
    lookup_field = "id"
    lookup_url_kwarg = "id_post"
    
class ListPostWithCommentsView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostWithCommentsSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id_post"