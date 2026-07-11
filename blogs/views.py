from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import ListModelMixin
from blogs.models import Category,Tag,Blog
from blogs.serializers import CategorySerializer, TagSerializer, BlogSerializer,CategoryNameSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,IsAdminUser, AllowAny
from blogs.permissions import IsAdminOrReporterOrEditor

class DeleteAndRestoreMinin:
    def perform_destroy(self, instance):
        instance.soft_delete()
        
    @action(detail=True, methods=['post'])
    def restore(self,request,pk=None):
        instance = self.get_object()
        instance.restore()
        return Response({'message':'object restore successfully'})
    
    
    @action(detail=True, methods=['delete'])
    def hard_delete(self, request,pk=None):
        instance = self.get_object()
        instance.hard_delete()
        return Response({'message':'object deleted successfully'})

class CategoryViewSet(DeleteAndRestoreMinin,ModelViewSet):
    """
    blogcategory viewset it include category crud operation
    """

    serializer_class = CategorySerializer
    #user admin is all category show others only active category
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Category.objects.all()
        if self.request.user.role =='admin':
            return Category.all_objects.all()
        
    
    def get_permissions(self):
        print('action',self.action)
        if self.action in ['create','update','partial_update','destroy','restore','hard_delete']:
            return [IsAdminUser()]
        return [AllowAny()]
        
    
class CategoryNameViewset(ListModelMixin,GenericViewSet):
    """Category name for blog form to category select"""
    queryset = Category.objects.all()
    serializer_class = CategoryNameSerializer



class TagViewSet(DeleteAndRestoreMinin, ModelViewSet):
    
    serializer_class = TagSerializer
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Tag.objects.all()
        if self.request.user.role in ['admin','report','editor']:
            return Tag.all_objects.all()
        
    
    
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [AllowAny()]
        return [IsAdminOrReporterOrEditor()]


class BlogViewSet(DeleteAndRestoreMinin,ModelViewSet):
    """
    Blog crud operation perform this viewset 
    list and retrieve anyuser and other operation another role user
    
    """
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Blog.objects.all()
        if self.request.user.role in ['admin','report','editor']:
            return Blog.all_objects.all()
        
        
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [AllowAny()]
        return [IsAdminOrReporterOrEditor()]
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    