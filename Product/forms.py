from django import forms
from .models import Product, Vote


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 'color', 'material', 'height', 'width', 'length', 'stockwerke',
                  'hoehlen', 'price']


class SearchForm(forms.ModelForm):
    name = forms.CharField(required=False)
    description = forms.CharField(required=False)
    brand = forms.CharField(required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'brand']


class SearchStarsForm(forms.ModelForm):
    stars = forms.IntegerField(required=False, max_value=5)

    class Meta:
        model = Vote
        fields = ['stars']
