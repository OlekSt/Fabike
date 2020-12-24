from django.urls import path
from . import views

urlpatterns = [
    path('bikes/', views.bikes, name="bikes"),
    path('<int:product_id>', views.bike, name="bike"),
    path('urban/', views.urban, name="urban"),
    path('all_road/', views.all_road, name="all_road"),
    path('road/', views.road, name="road"),
    path('frames/', views.frames, name="frames"),
    path('carbon/', views.carbon, name="carbon"),
    path('titanium/', views.titanium, name="titanium"),
]