from rest_framework import generics
from .models import Likes
from .serializers import LikeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from selecao_singolar.permissions import HasUserPermissions

# Create your views here.
class LikeCreateView(generics.CreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class ListCommentLikesView(generics.ListAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "comment"
    lookup_url_kwarg = "id_comment"
    
    def get_queryset(self):
        return Likes.objects.filter(comment=self.kwargs["id_comment"])
    
class LikeDestroyView(generics.DestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasUserPermissions]
    lookup_field = "comment"
    lookup_url_kwarg = "id_comment"
    
    def get_object(self):
        obj = Likes.objects.get(user=self.request.user, comment=self.kwargs["id_comment"])
        self.check_object_permissions(self.request, obj)
        return obj
    