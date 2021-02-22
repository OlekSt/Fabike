# some of the code was copied from Boutique Ado project's repository
# and modified according to the project's needs
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'purchase_date',
                       'delivery_cost', 'order_total',
                       'final_total', 'original_cart',
                       'stripe_pid',)
    # fields allows to specify the order of the fields in the admin interface
    fields = ('order_number', 'profile', 'full_name',
              'email', 'phone_number', 'address_line1', 'address_line2',
              'town_or_city', 'county', 'country',
              'postcode', 'purchase_date', 'delivery_cost',
              'order_total', 'final_total', 'original_cart',
              'stripe_pid')
    # restrict the columns that show up in the order list to only few key items
    list_display = ('order_number', 'purchase_date', 'full_name', 'profile',
                    'order_total', 'delivery_cost',
                    'final_total',)
    # displays most recent orders from the top
    ordering = ('-purchase_date',)

admin.site.register(Order, OrderAdmin)
