from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Menu(models.Model):
    meal_name = models.CharField(max_length=100)
    description = models.TextField()
    vegetarian_vegan = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.meal_name