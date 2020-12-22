from rest_framework import viewsets
from .location_models import (
    City,
    Country,
)
from location_selector_api.location_serializers import (
    CitySerializer,
    CountrySerializer,
)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
