from django.core.management.base import BaseCommand

from Product.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        return Category.objects.all()

    @staticmethod
    def json_read_products():
        return Product.objects.all()

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in self.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'], description=category['fields']['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['fields']['name'], description=product['fields']['description'],
                        photo=product['fields']['photo'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'],

                        ))

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
