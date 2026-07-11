

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import UserProfileViewSet
from blogs.views import CategoryViewSet,CategoryNameViewset,TagViewSet,BlogViewSet
from comments.views import CommentsViewSet


router  = DefaultRouter()
router.register(r'profile', UserProfileViewSet, basename='user-profile')
router.register('blog-categories',CategoryViewSet,basename='blog-category')
router.register('category-name',CategoryNameViewset,basename='category_name')
router.register('tags',TagViewSet,basename='tags')
router.register('blogs',BlogViewSet,basename='blogs')
router.register('comments',CommentsViewSet, basename='comments')


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include(router.urls)),
]


