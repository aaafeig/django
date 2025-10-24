from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = "Удаляет прошлые данные, и вставляет фикстуру в таблицу бд"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'category_fixture.json')
        self.stdout.write(self.style.SUCCESS('Данные из фикстуры с категориями были добавлены'))
        call_command('loaddata', 'product_fixture.json')
        self.stdout.write(self.style.SUCCESS('Данные из фикстуры с продуктами были добавлены'))