
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    family = models.BooleanField(default=False)
    action = models.BooleanField(default=False)
    adventure = models.BooleanField(default=False)
    animation = models.BooleanField(default=False)
    children = models.BooleanField(default=False)
    comedy = models.BooleanField(default=False)
    crime = models.BooleanField(default=False)
    documentary = models.BooleanField(default=False)
    drama = models.BooleanField(default=False)
    fantasy = models.BooleanField(default=False)
    film_noir = models.BooleanField(default=False)
    horror = models.BooleanField(default=False)
    musical = models.BooleanField(default=False)
    mystery = models.BooleanField(default=False)
    romance = models.BooleanField(default=False)
    sci_fi = models.BooleanField(default=False)
    thriller = models.BooleanField(default=False)
    war = models.BooleanField(default=False)
    western = models.BooleanField(default=False)
    imax = models.BooleanField(default=False)
