# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.views.generic.edit import UpdateView
from models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
