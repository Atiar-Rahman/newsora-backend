

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import UserProfileViewSet

router  = DefaultRouter()
router.register(r'profile', UserProfileViewSet, basename='user-profile')



urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include(router.urls)),
]


