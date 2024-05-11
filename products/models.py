from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    title = models.CharField(verbose_name='Name', max_length=50)
    description = models.TextField(blank=True)

class Product(models.Model):
    pass

class File(models.Model):
    pass