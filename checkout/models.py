# some of the code was copied from Boutique Ado project's repository
# and modified according to the project's needs
import uuid

from django.db import models
from django.conf import settings
from django.db.models import Sum

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import Profile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address_line1 = models.CharField(max_length=60, null=False, blank=False)
    address_line2 = models.CharField(max_length=60, null=True, blank=True)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    county = models.CharField(max_length=50, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=0,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=0,
                                      null=False, default=0)
    final_total = models.DecimalField(max_digits=10, decimal_places=0,
                                      null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates final total for an order.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.delivery_cost = 0
        self.final_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    product_color = models.CharField(max_length=10, null=True,
                                     blank=True)  # Red, Blue, Yellow, Black
    product_size = models.CharField(max_length=2, null=True,
                                    blank=True)  # XS, S, M, L, XL
    product_components = models.CharField(max_length=15, null=True,
                                          blank=True)  # alloy, carbon
    quantity = models.IntegerField(null=False, blank=False, default=0)
    price = models.DecimalField(max_digits=4, decimal_places=0,
                                null=True, blank=False)
    lineitem_total = models.DecimalField(max_digits=8, decimal_places=0,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.price * self.quantity
        super().save(*args, **kwargs)
