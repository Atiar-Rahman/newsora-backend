from rest_framework.serializers import ModelSerializer
from comments.models import  Comment

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
    