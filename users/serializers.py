from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer  
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CustomUserDetailsSerializer(UserDetailsSerializer):
    username=None
    
    """
    Custom serializer for user details.
    """
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('first_name', 'last_name', 'email','role','is_staff','is_active','joining_date')  # Add any additional fields you want to include in the user details response



class CustomRegisterSerializer(RegisterSerializer):
    username = None  # Remove username field

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        return {
            "email": self.validated_data.get("email", ""),
            "password1": self.validated_data.get("password1", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
        }

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.save()
        return user
    

class CustomLoginSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=True)
    