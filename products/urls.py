from django.urls import path
from . import views

urlpatterns = [
    path('bikes/', views.bikes, name="bikes"),
    path('products/', views.products, name="products"),
    path('<int:product_id>', views.product, name='product'),
    path('urban/', views.urban, name="urban"),
    path('all_road/', views.all_road, name="all_road"),
    path('road/', views.road, name="road"),
    path('frames/', views.frames, name="frames"),
]