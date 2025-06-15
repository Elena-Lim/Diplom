from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView, CommentCreateView, LikeCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
    path('posts/<int:post_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/likes/', LikeCreateView.as_view(), name='like-create'),
]