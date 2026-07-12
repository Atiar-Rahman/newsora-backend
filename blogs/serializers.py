from rest_framework.serializers import ModelSerializer
from blogs.models import Category, Blog,Tag, BlogImage
from rest_framework import serializers


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','slug','description','image','is_deleted','created_at','updated_at']
        read_only_fields = ['id','created_at','updated_at','slug']

class CategoryNameSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']
        read_ony_fields = ['id']

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','title','slug','created_at','updated_at']
        read_only_fields = ['id','slug','created_at','updated_at']
        
class BlogImageSerializer(ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = BlogImage
        fields = ['id','image','name','created_at','updated_at']
        read_only_fields = ['id','created_at','updated_at']

class BlogSerializer(ModelSerializer):
    image = BlogImageSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ['id','user','category','tags','title','slug','short_description','description','image','status','location','is_featured','views','comments_count','likes_count','published_at','meta_title','meta_description','created_at','updated_at']

        read_only_fields = ['id','user','slug','created_at','updated_at','image']        
        
    def create(self, validated_data):
        
        user = self.context.get('user')
        tags = validated_data.pop('tags', [])

        blog = Blog.objects.create(user=user,**validated_data)

        blog.tags.set(tags)

        return blog
    
    def update(self, instance, validated_data):

        tags = validated_data.pop('tags', None)

        instance = super().update(
            instance,
            validated_data
        )

        if tags is not None:
            instance.tags.set(tags)

        return instance
    
