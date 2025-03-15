from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Product, Category, Tag
from products.serializers.product_serializer import ProductSerializer
from products.serializers.category_serializer import CategorySerializer
from products.serializers.tag_serializer import TagSerializer
from rest_framework.generics import ListAPIView

class ProductListAPIView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        category_ids = request.GET.getlist('category')
        tag_ids = request.GET.getlist('tags')

        products = Product.objects.all()

        if query:
            products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

        if category_ids:
            products = products.filter(category_id__in=category_ids)

        if tag_ids:
            products = products.filter(tags__id__in=tag_ids).distinct()

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer