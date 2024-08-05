from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views import PostViewSet

from post.views import PostCreateView,PostListView


router = DefaultRouter()
router.register(r'records', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('postsrecords/', PostCreateView.as_view(), name='post-create'),

    path('postlist/', PostListView.as_view(), name='postlist'),
    # path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

]
