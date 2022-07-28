from django import forms
from .models import Product, Vote, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 'color', 'height', 'width', 'length',
                  'price', 'product_picture']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
        widgets = {
            'user': forms.HiddenInput(),
            'product': forms.HiddenInput(),
        }


class SearchForm(forms.ModelForm):
    name = forms.CharField(required=False)
    description = forms.CharField(required=False)
    brand = forms.CharField(required=False)
    height = forms.IntegerField(required=False, max_value=100, min_value=0)
    width = forms.IntegerField(required=False, max_value=500, min_value=0)
    length = forms.IntegerField(required=False, max_value=500, min_value=0)
    price = forms.IntegerField(required=False,  min_value=0)

    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 'height']


class SearchStarsForm(forms.ModelForm):
    stars = forms.IntegerField(required=False, max_value=5, min_value=1)

    class Meta:
        model = Vote
        fields = ['stars']
