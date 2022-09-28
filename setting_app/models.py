from email.mime import image
from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length= 30 , verbose_name= "Category")

    def __str__(self):
        return self.title



class Meals(models.Model):
    title = models.CharField(max_length= 40 , verbose_name= "Называния Блюда")
    discription = models.TextField(verbose_name= "Приготовлени Блюда")
    image = models.ImageField(upload_to='setting_app', verbose_name= "Image")
    category = models.ForeignKey(Category, verbose_name= 'Category', on_delete = models.CASCADE)

