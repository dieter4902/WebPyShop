from django import forms
from Product.models import Comment


class CommentEditForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'comment_id': forms.HiddenInput(),
        }