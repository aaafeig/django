from django.shortcuts import render
from .models import Product

# Create your views here.

def contacts(request):
    if request.method == "GET":
        return render(request, 'contacts.html')


def home(request):
    products = Product.objects.all()
    context = {
        "products": products
    }

    return render(request, "home.html", context=context)

def product_details(request, product_id=1):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }

    return render(request, "product_details.html", context=context)