from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('stock_info/', views.stock_info, name='search')
]