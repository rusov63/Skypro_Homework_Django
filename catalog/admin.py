from django.contrib import admin
from catalog.models import Category, Product, Blog

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Админ-панель модели - Product'''
    list_display = ('id', 'name', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Админ-панель модели - Category'''
    list_display = ('id', 'name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    '''Админ-панель модели - Blog'''
    list_display = ('id', 'name', 'number_views', 'content')
    search_fields = ('name', 'content')
    list_filter = ('content',)
    prepopulated_fields = {"slug": ("name",)}

#prepopulated_fields - обрабатывает заголовок в реальной времени в админ панеле

