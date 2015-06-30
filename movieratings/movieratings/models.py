from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=20)
    spicy = models.BooleanField(default=False)


class Person(models.Model):
    name = models.CharField(max_length=100)
    favorite_food = models.ForeignKey(Food)
