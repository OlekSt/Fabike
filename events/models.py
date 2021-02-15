from django.db import models
from django.core.validators import MinValueValidator


class Event(models.Model):

    title =	models.CharField(max_length=120)
    topics = models.CharField(max_length=240, null=False, blank=False)
    learning = models.TextField(max_length=240, null=False, blank=False)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    address = models.CharField(max_length=60, null=False, blank=False)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    map_link = models.URLField(max_length=1024, null=True, blank=True)
    price = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=False, 
                                       validators=[MinValueValidator(1)])
    comment = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.title
