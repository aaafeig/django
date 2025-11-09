from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import Product

# Create your views here.

# Создайте новый контроллер и шаблон
# для
# отображения
# страницы
# с
# подробной
# информацией
# о
# товаре.На
# этой
# странице
# должна
# быть
# показана
# вся
# информация
# о
# товаре.


def home(request):
    if request.method == "GET":
        return render(request, 'home.html')


def contacts(request):
    if request.method == "GET":
        return render(request, 'contacts.html')

def product_details(request, product_id=1):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }

    return render(request, "product_details.html", context=context)