from rest_framework import serializers
from products.models import Product

# My architecture needs that Product returns id, name, description, price, category id, category name
# and the list of related tags. To do this, we first need to serialize the category ID, name, and tags. 
# Once this is done, we can assemble it.

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source="category.id", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category_id', 'category_name', 'tags', 'price']