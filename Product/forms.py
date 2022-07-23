from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 'color', 'material', 'height', 'width', 'length', 'stockwerke',
                  'hoehlen', 'price']


class SearchForm(forms.ModelForm):
    name = forms.CharField(required=False)
    description = forms.CharField(required=False)

    class Meta:
        model = Product
        fields = ['name', 'description']

