from django.urls import path
from .views import ProductListAPIView, CategoryListAPIView, TagListAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('tags/', TagListAPIView.as_view(), name='tag-list'),
]
