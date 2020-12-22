from rest_framework import viewsets
from .models_hotel import (
    Hotel,
    Category,
)
from hotel_selector_api.serializers_hotel import HotelSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
