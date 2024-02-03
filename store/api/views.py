from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from products.models import Product, Basket
from products.serializers import ProductSerializer, BasketSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BasketModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer