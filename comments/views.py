from rest_framework.viewsets import ModelViewSet
from blogs.views import DeleteAndRestoreMinin
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated


class CommentsViewSet(DeleteAndRestoreMinin, ModelViewSet):
    
    """this Comment ViewSets are Crud operation any user see all comments admin see all comments. list and retrieve any user resoter and harddelete must be admin user and other operation must be authenticated user"""
    
    
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Comment.objects.all()
        if self.request.user.role == 'admin':
            return Comment.all_objects.all()
        
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [AllowAny()]
        if self.action in ['restore','hard_delete']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    

