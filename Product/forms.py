from django import forms
from .models import Product, Vote, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 'color', 'material', 'height', 'width', 'length', 'stockwerke',
                  'hoehlen', 'price', 'product_picture', 'product_file']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'user': forms.HiddenInput(),
            'product': forms.HiddenInput(),
        }


class SearchForm(forms.ModelForm):
    name = forms.CharField(required=False)
    description = forms.CharField(required=False)
    brand = forms.CharField(required=False)
    MATERIALS = [
        ("", ""),
        ("p", "Plüsch"),
        ("s", "Samt")
    ]
    material = forms.ChoiceField(initial='', choices=MATERIALS, required=False, )

    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 'material']


class SearchStarsForm(forms.ModelForm):
    stars = forms.IntegerField(required=False, max_value=5)

    class Meta:
        model = Vote
        fields = ['stars']
