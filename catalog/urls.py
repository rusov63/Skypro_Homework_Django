from django.urls import path
from catalog.apps import MainConfig
from catalog.views import index, contacts, \
    ProductsListView, ProductsDetailView, BlogListView, \
    BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, toggle_activity

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductsListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductsDetailView.as_view(), name='product_item'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_item'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/update/<slug:slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/delete/<slug:slug>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blogs/toggle/<slug:slug>/', toggle_activity, name='toggle_activity'),

]



