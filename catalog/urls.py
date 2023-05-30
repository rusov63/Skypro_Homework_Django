from django.urls import path
from catalog.apps import MainConfig
from catalog.views import index, contacts, products, product_card

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='product_list'),
    path('product_card/<str:pk>/', product_card, name='product_item'),
]



