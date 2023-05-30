from django.shortcuts import render
from catalog.models import Category, Product


def index(request):
    """Главная страница, выводит четыре товара"""
    context = {
        'product_list': Product.objects.all()[:4],
        'title': "JBT"
    }
    return render(request, 'catalog/index.html', context)

def products(request):
    """Полный список товара"""
    context = {
        'product_list': Product.objects.all,
        'title': "Тормозные суппорта - JBK"
    }
    return render(request, 'catalog/products.html', context)

def product_card(request, pk):
    """Карточка товара"""
    product_item = Product.objects.get(pk=pk)
    context = {
        'object': product_item,
        'title': product_item
    }
    return render(request, 'catalog/product_card.html', context)


def contacts(request):
    """Страница с контактами"""
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Пользователь {name} оставил контактный телефон {phone} и сообщение: {message}')

    context = {
        'title': "Контакты"
    }
    return render(request, 'catalog/contacts.html', context)

