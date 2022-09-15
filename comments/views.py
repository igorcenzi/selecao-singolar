from rest_framework import generics
from .serializers import CommentSerializer
from .models import Comments
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from selecao_singolar.permissions import HasUserPermissions

# Create your views here.

class CommentsCreateListView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class PostCommentsListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "post"
    lookup_url_kwarg = "post_id"

    def get_queryset(self):
        return Comments.objects.filter(post=self.kwargs["post_id"])
    
class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasUserPermissions]
    lookup_field = "id"
    lookup_url_kwarg = "comment_id"