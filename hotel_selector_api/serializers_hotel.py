from rest_framework import serializers
from location_selector_api.serializers_location import CitySerializer, CountrySerializer
from .models_hotel import (
    Hotel,
    Category,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]


class HotelSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Hotel
        fields = ("hotel_name", "slug", "image", "city", "country", "category", "price")
