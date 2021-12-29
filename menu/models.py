from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Menu(models.Model):
    meal_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)    
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    vegetarian_vegan = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField()

    class Meta:
        verbose_name = "meal"
        verbose_name_plural = 'meals'

    def __str__(self):
        return self.meal_name

        
class Category(models.Model):
    meal_category = models.CharField(max_length=50)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.meal_category
