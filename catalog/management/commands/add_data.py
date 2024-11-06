from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add test product and category to the database"

    def handle(self, *args, **kwargs):
        # Удаляем данные перед загрузкой
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загрузка данных из фикстуры
        call_command("loaddata", "products_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
