""# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from autoslug import AutoSlugField

from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    label = models.CharField(max_length = 50)

    def __unicode__(self):
        return "Category : %s" % self.label

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"



class Post(models.Model):

    title = models.CharField(verbose_name="le titre du boss", max_length = 30)
    body = RichTextField()
    creation_date = models.DateTimeField(auto_now_add = True)
    slug = AutoSlugField(populate_from='title', always_update=True, unique_with = ("title",))

    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
