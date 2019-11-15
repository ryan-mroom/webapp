from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='newsfeed-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='newsfeed-post-detail'),
    path('post/new/', PostCreateView.as_view(), name='newsfeed-post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='newsfeed-post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='newsfeed-post-delete'),
]