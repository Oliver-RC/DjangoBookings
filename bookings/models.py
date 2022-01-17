from django.db import models
from django.contrib.auth.models import User


class Tables(models.Model):
    TABLE_CHOICES = (
        ('2', '2'),
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
        ('10+', '10+'),
    )

    table_size = models.CharField(max_length=200, null=True, choices=TABLE_CHOICES, default='2')

    class Meta:
        verbose_name = "table"
        verbose_name_plural = 'tables'

    def __str__(self):
        return self.table_size


class Booking(models.Model):
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

    STATUS = (
        ('Booking awaiting restaurant confirmation', 'Booking awaiting restaurant confirmation'),
        ('Booking confirmed', 'Booking confirmed'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    requirements = models.TextField(blank=True, null=True)
    table_size = models.ForeignKey(Tables, null=True, on_delete=models.SET_DEFAULT, default='2')
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_CHOICES, default='12:00')
    status = models.CharField(max_length=50, choices=STATUS, default='Booking awaiting restaurant confirmation')

    class Meta:
        ordering = ['status']

    def __str__(self):
        return self.first_name