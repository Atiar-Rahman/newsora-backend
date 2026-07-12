from django.contrib import admin
from blogs.models import Category, Tag, Blog, BlogImage
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    list_filter = ['title']
    search_fields=['tile']
    
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['title']
    list_filter=['title']
    search_fields = ['title']

@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display=['name','image']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','category','short_description']
    list_filter = ['title','user','category']
    search_fields = ['title','user','category']
    
    
