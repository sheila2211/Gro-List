from django import forms
from .models import Post

class PostForm(forms.Form):

    text = forms.CharField()
    post_type = forms.ChoiceField()
    neccessity = forms.BooleanField()