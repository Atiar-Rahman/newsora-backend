from rest_framework.serializers import ModelSerializer
from comments.models import  Comment, BlogReaction,CommentReaction,Bookmark, BlogView,Subscriber

class ReplySerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "comment",
            "created_at"
        ]


class CommentSerializer(ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = ['id','user','blog','parent','comment','replies','is_approved','likes_count','replies_count','created_at','updated_at']
        
        read_only_fields = ['id','user','is_approved','likes_count','replies_count','created_at','updated_at']
        
    def create(self, validated_data):
        user = self.context['request'].user
        return Comment.objects.create(user=user, **validated_data)



class BlogReactionSerializer(ModelSerializer):
    class Meta:
        model = BlogReaction
        fields = ['id','user','blog','reaction','created_at','updated_at']
        read_only_fields = ['id','user','created_at','updated_at']
        
    def create(self, validated_data):
        user = self.context['request'].user
        
        return BlogReaction.objects.create(user=user, **validated_data)
    


class CommentReactionSerializer(ModelSerializer):
    class Meta:
        model = CommentReaction
        fields = ['id','user','comment','reaction','created_at','updated_at']
        read_only_fields = ['id','user','created_at','updated_at']
        
    
    def create(self, validated_data):
        user = self.context['request'].user
        
        return CommentReaction.objects.create(user=user, **validated_data)
    


class BookmarkSerializer(ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id','user','blog','created_at','updated_at']
        read_only_fields = ['id','user','created_at','updated_at']
        
    def create(self, validated_data):
        user = self.context['request'].user
        
        return Bookmark.objects.create(user=user, **validated_data)
    

class BlogViewSerializer(ModelSerializer):
    class Meta:
        model = BlogView
        fields = ['id','user','blog','ip_address','user_agent','created_at','updated_at']
        read_only_fields = ['id','user','created_at','updated_at']
        

class SubscriberSerializer(ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['id','email','is_active','created_at','updated_at']
        read_only_fields = ['id','email','created_at','updated_at']

