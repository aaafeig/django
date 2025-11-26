from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','description', 'image', 'category', 'price']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        ban_words = ['казино','криптовалюта','крипта','биржа','дешево','бесплатно','обман','полиция','радар']
        if title.lower() in ban_words:
            raise ValidationError('В название есть запрещенные слова')
        return title
