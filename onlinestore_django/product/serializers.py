from rest_framework import serializers
from .models import Category, Product


# serializers is used to get data from the database and turn them into json
# so they can be used in the frontend

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # because you want to use product to get infomation
        model = Product
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumbnail',
        ) 

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        # because you want to use product to get infomation
        model = Category
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'products',
        ) 