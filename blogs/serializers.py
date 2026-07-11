from rest_framework.serializers import ModelSerializer
from blogs.models import Category, Blog,Tag

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
    

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','user','category','tags','title','slug','short_description','description','image','status','location','is_featured','views','comments_count','likes_count','published_at','meta_title','meta_description','created_at','updated_at']

        read_only_fields = ['id','user','slug','created_at','updated_at']        
        
    def create(self, validated_data):
        tags = validated_data.pop('tags', [])

        blog = Blog.objects.create(**validated_data)

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
    
