from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Подробное описание товара',
            'rows': 4
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-select'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })

    def clean_title(self):
        title = self.cleaned_data.get('title')
        ban_words = ['казино','криптовалюта','крипта','биржа','дешево','бесплатно','обман','полиция','радар']
        if title.lower() in ban_words:
            raise ValidationError('В название есть запрещенные слова')
        return title

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Цена может быть только больше нуля')
        return price