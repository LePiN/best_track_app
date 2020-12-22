from rest_framework import serializers
from .location_models import (
    City,
    Country,
)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["name", "slug"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["name", "slug", "state"]
