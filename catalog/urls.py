from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('', views.ProductListView.as_view(), name='product-list-view'),
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product_create/', views.ProductCreateView.as_view(), name='product-create'),
    path('product_update/<int:pk>', views.ProductUpdateView.as_view(), name='product-update'),
    path('product_delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
]