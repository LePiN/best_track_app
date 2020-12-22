from rest_framework import viewsets
from .hotel_models import (
    Hotel,
    Category,
)
from hotel_selector_api.hotel_serializers import HotelSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
