from django.db import models
from location_selector_api.models_location import City, Country


class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    class Meta:
        db_table = "hotel"

    hotel_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.URLField()
    price = models.IntegerField(default=0)
    city = models.ForeignKey(City, related_name="hotels", on_delete=models.CASCADE)
    country = models.ForeignKey(
        Country, related_name="hotels", on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category, related_name="hotels", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.hotel_name}, {self.price}, {self.city}, {self.country}, {self.category}"
