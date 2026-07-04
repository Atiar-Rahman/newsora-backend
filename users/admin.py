from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User, Profile
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {
            'fields': ('first_name', 'last_name',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'role', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined')
    
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'birth_date')
    search_fields = ('user__email', 'bio', 'location')
    ordering = ('user__email',)
    