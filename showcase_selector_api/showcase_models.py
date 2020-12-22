from django.db import models
from hotel_selector_api.hotel_models import Hotel


class PageRoute(models.Model):

    page_identifier = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.page_identifier

    class Meta:
        db_table = "page_route"


class Showcase(models.Model):

    STATUS_CHOICES = [("A", "ACTIVE"), ("B", "BUILDING"), ("I", "INACTIVE")]

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, unique=True)
    routes = models.ManyToManyField(PageRoute)
    itens = models.ManyToManyField(Hotel)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="B")

    class Meta:
        db_table = "showcase"
        ordering = ["title", "subtitle"]
