from django.contrib import admin
from comments.models import Comment, BlogReaction,CommentReaction, Bookmark,BlogView,Subscriber
# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','blog','is_approved']
    list_filter = ['is_approved','blog']
    search_fields = ['comment','blog']


@admin.register(BlogReaction)
class BlogReactionAdmin(admin.ModelAdmin):
    list_display = ['user','blog','reaction']
    list_filter = ['blog','reaction']
    search_fields = ['reaction','blog']
    
    

@admin.register(CommentReaction)
class CommentReactionAdmin(admin.ModelAdmin):
    list_display = ['user','comment','reaction']
    list_filter = ['reaction']
    search_fields = ['comment']
    
    
    
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['user','blog']
    list_filter = ['user','blog']
    search_fields = ['user','blog']
    
    
    
@admin.register(BlogView)
class BlogViewAdmin(admin.ModelAdmin):
    list_display = ['user','blog','ip_address']
    list_filter = ['user','blog']
    search_fields = ['user','blog']
    
    
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email','is_active']
    list_filter = ['email','is_active']
    search_fields = ['email']
    