from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Название')
    description = models.TextField(verbose_name = 'Описание')
    

    def __str__(self):
        return f"{self.title}: {self.description}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title', ]

class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Название')
    description = models.TextField(verbose_name = 'Описание')
    image = models.ImageField(verbose_name = 'Изображение', null=True, blank=True, upload_to='product_image/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = 'категория')
    price = models.IntegerField(verbose_name = 'Цена')
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'''Название: {self.title}
        описание: {self.description}
        цена: {self.price}
        '''

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['title',]