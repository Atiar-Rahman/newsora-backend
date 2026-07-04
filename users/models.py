from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from core.models import BaseModel
from users.managers import CustomUserManager 
# Create your models here.


class User(AbstractUser, BaseModel):
    class Rolechoices(models.TextChoices):
        USER = 'user'
        ADMIN = 'admin'
        REPORTER = 'report'
        EDITOR = 'editor'
    username=None
    email=models.EmailField(unique=True)
    role = models.CharField(max_length=50,default=Rolechoices.USER, choices=Rolechoices.choices)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    joining_date = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    
    def __str__(self):
        return self.email
    
    

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    present_address = models.TextField(blank=True)
    permanent_address = models.TextField(blank=True)
    office_address = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.email}'s profile"