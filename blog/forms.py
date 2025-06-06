from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget

class PostEdit(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
        widgets = {
            'content': SummernoteWidget(),
        }
