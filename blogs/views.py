from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import ListModelMixin
from blogs.models import Category,Tag,Blog,BlogImage
from blogs.serializers import CategorySerializer, TagSerializer, BlogSerializer,CategoryNameSerializer, BlogImageSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,IsAdminUser, AllowAny
from blogs.permissions import IsAdminOrReporterOrEditor
from comments.models import BlogView, Bookmark


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


class BlogImageViewSet(DeleteAndRestoreMinin, ModelViewSet):
    """Blog image crud api make it can heve to one blog multiple bolg"""
    serializer_class =  BlogImageSerializer
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Blog.objects.all()
        if self.request.user.role in ['admin','report','editor']:
            return Blog.all_objects.all()
        
        
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
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context
    
    @action(detail=True, methods=['post'])
    def bookmark(self, request, pk=None):

        blog = self.get_object()

        bookmark, created = Bookmark.objects.get_or_create(
            user=request.user,
            blog=blog
        )

        if created:
            message = "Blog added to bookmark"
        else:
            message = "Already bookmarked"

        return Response({
            "message": message
        })
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):

        blog = self.get_object()

        blog.status = "published"
        blog.save()

        return Response({
            "message": "Blog published"
        })
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_authenticated:
            BlogView.objects.get_or_create(
                user=request.user,
                blog=instance,
                defaults={
                    "ip_address": request.META.get("REMOTE_ADDR", ""),
                    "user_agent": request.META.get("HTTP_USER_AGENT", "")
                }
            )

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
        

       