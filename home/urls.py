from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('under_construction/', views.under_construction,
         name='under_construction'),
]
