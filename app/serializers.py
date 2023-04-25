from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    category = CategorySerializer()

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get(name=category_data['name'])
        return Product.objects.create(category=category, **validated_data)

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get(name=category_data['name'])
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.category = category
        instance.save()
        return instance