from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
]