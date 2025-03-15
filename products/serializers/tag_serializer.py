from rest_framework import serializers
from products.models import Tag

# Parse id and name of Model Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']