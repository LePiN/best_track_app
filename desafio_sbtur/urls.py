from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from showcase_selector_api.showcase_views import ShowcaseViewSet, PageRouterViewSet
from hotel_selector_api.hotel_views import HotelViewSet, CategoryViewSet
from location_selector_api.location_views import (
    CityViewSet,
    CountryViewSet,
)

route = routers.DefaultRouter()
route.register(r"city", CityViewSet, basename="city")
route.register(r"hotel", HotelViewSet, basename="hotel")
route.register(r"country", CountryViewSet, basename="country")
route.register(r"showcase", ShowcaseViewSet, basename="showcase")
route.register(r"category", CategoryViewSet, basename="category")
route.register(r"page_route", PageRouterViewSet, basename="page_route")

urlpatterns = [path("admin/", admin.site.urls), path("", include(route.urls))]
