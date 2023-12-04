from django.forms import ModelForm
from django import forms

from forum.models import Post

class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

    class Meta:
        model = Post
        fields = '__all__'