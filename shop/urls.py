from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),  
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/create/', product_create, name='product_create'),
    path('add/<int:product_id>/', add_product, name="add_product"),
    path('delete/<int:product_id>/', delete_product, name="delete_product"),
    path('subtract/<int:product_id>/', subtract_product, name="subtract_product"),
    path('clear/', clear_card, name="clear_card"),
]
