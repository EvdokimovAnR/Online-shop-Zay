from rest_framework import serializers

from products.models import Product
from products.models import Basket

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category')

class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Basket
        fields = ('id', 'product', 'quantity', 'created_timestamp', 'summa')
        read_only_fields = ('created_timestamp',)