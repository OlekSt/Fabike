from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'date', 
        'title',
        'topics',
        'date',
        'time',
        'price',
    )

    ordering = ('date',)

# Register your models here.
admin.site.register(Event, EventAdmin)
