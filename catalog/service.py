from .models import Product


class ProductService:

    @staticmethod
    def sort_products(category_id: int) -> [str]:
        list_sort_products = Product.objects.filter(category=category_id)
        return list_sort_products