from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Пользователь {name} оставил контактный телефон {phone} и сообщение: {message}')
    return render(request, 'catalog/contacts.html')

def media(request):
    return render(request, 'catalog/media.html')
