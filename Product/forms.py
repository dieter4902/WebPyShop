from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from .models import Product, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'description', 'brand', 'color', 'height', 'width', 'length', 'price', 'product_picture', 'product_file']
        fields = ['name', 'description', 'brand', 'color', 'height', 'width', 'length', 'price', 'product_picture']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'  # get or post
            self.helper.layout = Layout(
                Row(
                    # col-md-3 = column medium block 3
                    # mb-0 = margin bottom 0
                    Column('name', css_class='form-group col-md-2 mb-0'),
                    Column('brand', css_class='form-group col-md-1 mb-0'),
                    css_class='form-row'
                ),
                'description',
                Row(
                    Column('height', css_class='form-group col-md-1 mb-0'),
                    Column('width', css_class='form-group col-md-1 mb-0'),
                    Column('length', css_class='form-group col-md-1 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('color', css_class='form-group col-md-1 mb-0'),
                    Column('price', css_class='form-group col-md-1 mb-0'),
                    css_class='form-row'
                ),
                'product_picture',
                Submit('submit', 'Add new book')
            )


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
    price = forms.IntegerField(required=False, min_value=0)
    stars = forms.IntegerField(required=False, max_value=5, min_value=0)

    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 'stars']

# class SearchStarsForm(forms.ModelForm):
#    stars = forms.IntegerField(required=False, max_value=5, min_value=1)
#
#    class Meta:
#        model = Product
#        fields = ['stars']
