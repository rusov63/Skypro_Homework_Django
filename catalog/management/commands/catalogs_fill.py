from django.core.management import BaseCommand
from catalog.models import Category

class Command(BaseCommand):
    """Класс для заполнения каталогов, catalog_product.json"""

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Суппорты', 'description': 'Тормоза'},
        ]

        catalogs_objects = []
        for catalog_item in category_list:
            catalogs_objects.append(Category(**catalog_item))

        Category.objects.bulk_create(catalogs_objects)
