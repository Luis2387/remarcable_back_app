from rest_framework import serializers
from products.models import Category

# Parse id and name of Model Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']