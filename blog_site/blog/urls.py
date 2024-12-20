from django.urls import path,include 
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet,CommentViewSet,RegisterView,LoginView

router = DefaultRouter()
router.register('blog-posts',BlogPostViewSet,basename='blogpost')
router.register('comments',CommentViewSet,basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login')
]