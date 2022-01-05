from django.db import models
from django.contrib.auth.models import User


TIME_CHOICES = (
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
)


class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    requirements = models.TextField(blank=True, null=True)
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_CHOICES, default='12:00')

    def __str__(self):
        return self.first_name