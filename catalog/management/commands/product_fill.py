from django.core.management import BaseCommand
from catalog.models import Product

class Command(BaseCommand):
    """Класс для заполнения товара, product_product.json"""

    def handle(self, *args, **options):
        product_list = [
            {'name': 'Домкрат 2Т Gigant T83502',
             'description': 'Гидравлический подкатной домкрат в кейсе обеспечивает плавное поднятие автомобиля на высоту '
                            'до 330 мм во время замены колеса.',
             'category': 'Автотовары',
             'price': 8987, 'creation_at': '2021-01-01', 'modified_at': '2021-01-01'},

            {'name': 'Домкрат Gigant 3 т HTJ-3SL',
             'description': 'Гидравлический супернизкий подкатной домкрат обеспечивает плавное '
                            'поднятие автомобиля на высоту до 508 мм для проведения шиномонтажных работ.',
             'category': 'Автотовары', 'price': 9918, 'creation_at': '2022-01-01', 'modified_at': '2022-01-01'},

            {'name': 'Домкрат Gigant 5Т HBJ-5',
             'description': 'Гидравлический бутылочный домкрат подойдет для легковых автомобилей, '
                            'внедорожников и малотоннажных грузовиков.',
            'category': 'Автотовары', 'price': 1638, 'creation_at': '2022-02-01', 'modified_at': '2022-02-01'},
        ]

        products_objects = []
        for product_item in product_list:
            products_objects.append(Product(**product_item))

        Product.objects.bulk_create(products_objects)
