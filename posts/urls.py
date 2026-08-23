from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('create/', views.post_create_view, name='post_create'),
    path('<slug:post_slug>/', views.post_detail_view, name='post_detail'),
    path('<slug:post_slug>/update/', views.post_update_view, name='post_update'),
    path('<slug:post_slug>/delete/', views.post_delete_view, name='post_delete'),
    path('<slug:post_slug>/like/', views.post_like_toggle_view, name='post_like'),
]
