from rest_framework import serializers
from hotel_selector_api.hotel_serializers import HotelSerializer
from .showcase_models import Showcase, PageRoute


class PageRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageRoute
        fields = ["page_identifier"]


class ShowCaseSerializer(serializers.ModelSerializer):
    routes = PageRouteSerializer(many=True)
    itens = HotelSerializer(many=True)

    def to_representation(self, instance):
        data = super(ShowCaseSerializer, self).to_representation(instance)
        data["routes"] = [value["page_identifier"] for value in data["routes"]]
        return data

    class Meta:
        model = Showcase
        ordering = "id"
        fields = ("id", "title", "subtitle", "routes", "itens")
