from django.db import models


class PizzaOrder(models.Model):
    CHOICES = [
        ('margherita', 'Margherita'),
        ('pepperoni', 'Pepperoni'),
        ('vegetarian', 'Vegetarian'),
        ('hawaiian', 'Hawaiian'),
    ]

    pizza_type = models.CharField(max_length=20, choices=CHOICES)
    comments = models.TextField(blank=True)
