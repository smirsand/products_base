from django.core.management import BaseCommand

from products_app.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {"name_category": "фрукты",
             "description_category": "1 сорт"
             },
            {"name_category": "овощи",
             "description_category": "1 сорт"
             },
            {"name_category": "ягоды",
             "description_category": "спелые"
             }
        ]

        category_for_create = []
        for i in category_list:
            category_for_create.append(Category(**i))

        Category.objects.bulk_create(category_for_create)

        products_list = [
            {"product_name": "яблоко",
             "description": "текст",
             "image": "",
             "category": Category.objects.get(name_category="фрукты"),
             "price": "100.00",
             "date_of_creation": "2023-08-31T17:41:08Z",
             "date_of_change": "2023-08-31T17:41:09Z"
             },
            {"product_name": "картофель",
             "description": "текст",
             "image": "",
             "category": Category.objects.get(name_category="овощи"),
             "price": "120.00",
             "date_of_creation": "2023-08-31T17:41:00Z",
             "date_of_change": "2023-08-31T17:41:02Z"
             },
            {"product_name": "вишня",
             "description": "текст",
             "image": "",
             "category": Category.objects.get(name_category="овощи"),
             "price": "250.00",
             "date_of_creation": "2023-08-31T17:40:51Z",
             "date_of_change": "2023-08-31T17:40:52Z"
             }
        ]

        product_for_create = []
        for product in products_list:
            product_for_create.append(Product(**product))

        Product.objects.bulk_create(product_for_create)
