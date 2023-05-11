from django.urls import path
from catalog.apps import MainConfig
from catalog.views import index, contacts, media

app_name = MainConfig.name

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('media/', media)
]



