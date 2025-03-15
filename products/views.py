from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Product, Category, Tag
from products.serializers.product_serializer import ProductSerializer
from products.serializers.category_serializer import CategorySerializer
from products.serializers.tag_serializer import TagSerializer
from rest_framework.generics import ListAPIView


# In the API of product, we receive the url created in react, example: 
# http://127.0.0.1:8000/api/products/?category=1&category=4&tags=2&tags=10

class ProductListAPIView(APIView):
    def get(self, request):
    	# get and getlist will save the variables that are on the url on their respective variables
        query = request.GET.get('q', '')
        category_ids = request.GET.getlist('category')
        tag_ids = request.GET.getlist('tags')

        # Retreive all the products
        products = Product.objects.all()

        # If there is q="something" in the url, then we will use query to search in the queryset
        # in the name and in the description using icontains and Q so we can join then with an OR

        if query:
            products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

        # Filter the products that have the the same category id as the one in the list of ids provided

        if category_ids:
            products = products.filter(category_id__in=category_ids)


        # Filter the products that have the the same tag id as the one in the list of ids provided
        # Unlike category, disctinct is use here to prevent duplicates because there can be
        # Products with multiple tags

        if tag_ids:
            products = products.filter(tags__id__in=tag_ids).distinct()


        # Once the queryset is filtered, we give it to ProductSerializer to parse it to json and
        # return the API response
        
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# For category and tag the API is simple. I'm using ListAPIView, that will handle the return of a
# list by default

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer