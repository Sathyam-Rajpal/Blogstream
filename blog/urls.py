from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    )
from . import views
urlpatterns = [
    # localhost:8000/
    path('',PostListView.as_view(), name='home'),    
    path('user/<str:username>',UserPostListView.as_view(), name='user_posts'),    
    path('post/<int:pk>/',PostDetailView.as_view(), name='post_details'),        
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post_update'),        
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post_delete'),        
    path('post/new/',views.PostCreateView.as_view(), name='post_create'),    
    path('about/',views.about, name='about'),    

]
