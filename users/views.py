from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from users.models import Profile
from users.serializers import UserProfileSerializer 
# Create your views here.

class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer 
    
    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)   
    
