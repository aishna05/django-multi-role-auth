from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.create_blog_post, name='create_blog'),
    path('doctor-posts/', views.doctor_posts, name='doctor_posts'),
    path('posts/', views.blog_post_list, name='blog_post_list'),
    path('edit/<int:post_id>/', views.edit_blog_post, name='edit_blog_post'),
    path('toggle-draft/<int:post_id>/', views.toggle_draft_status, name='toggle_draft'),
    path('delete/<int:post_id>/', views.delete_blog_post, name='delete_blog'),
    path('posts/<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
]
