from rest_framework.viewsets import ModelViewSet
from blogs.views import DeleteAndRestoreMinin
from comments.models import Comment,BlogReaction,CommentReaction, Bookmark, BlogView,Subscriber
from comments.serializers import CommentSerializer, BlogReactionSerializer,CommentReactionSerializer, BookmarkSerializer,BlogViewSerializer, SubscriberSerializer
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated


class PermissionMixin:
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [AllowAny()]
        
        if self.action in ['restore','hard_delete']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

class CommentsViewSet(DeleteAndRestoreMinin,PermissionMixin, ModelViewSet):
    
    """this Comment ViewSets are Crud operation any user see all comments admin see all comments. list and retrieve any user resoter and harddelete must be admin user and other operation must be authenticated user"""
    
    
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Comment.objects.all()
        if self.request.user.role == 'admin':
            return Comment.all_objects.all()
        
    
    


class BlogReactionViewSet(DeleteAndRestoreMinin, PermissionMixin, ModelViewSet):
    serializer_class = BlogReactionSerializer
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return BlogReaction.objects.all()
        
        if self.request.user.role=='admin':
            return BlogReaction.all_objects.all()
        
    
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [AllowAny()]
        
        if self.action in ['restore','hard_delete']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    
class CommentReactionViewSet(DeleteAndRestoreMinin, PermissionMixin, ModelViewSet):
    serializer_class = CommentReactionSerializer
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return CommentReaction.objects.all()
        
        if self.request.user.role == 'admin':
            return CommentReaction.all_objects.all()
        
    
    
    
class BookmarkViewSet(DeleteAndRestoreMinin, PermissionMixin, ModelViewSet):
    serializer_class = BookmarkSerializer
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Bookmark.objects.none()
        
        if self.request.user.is_authenticated:
            return Bookmark.objects.filter(user = self.request.user)
        
        if self.request.user.role == 'admin':
            return Bookmark.all_objects.all()
        
    

class BlogViewViewSet(DeleteAndRestoreMinin, PermissionMixin, ModelViewSet):
    http_method_names=['get','post']
    serializer_class = BlogViewSerializer
    
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return BlogView.objects.none()
        
        if self.request.user.is_authenticated:
            return BlogView.objects.filter(user = self.request.user)
        
        if self.request.user.role == 'admin':
            return BlogView.all_objects.all()



class SubscriberViewSet(DeleteAndRestoreMinin, PermissionMixin, ModelViewSet):
    serializer_class = SubscriberSerializer
    
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Subscriber.objects.none()
        
        if self.request.user.is_authenticated:
            return Subscriber.objects.filter(user = self.request.user)
        
        if self.request.user.role == 'admin':
            return Subscriber.all_objects.all()


