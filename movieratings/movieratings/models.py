from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=20)
    spicy = models.BooleanField(default=False)


class Person(models.Model):
    name = models.CharField(max_length=100)
    favorite_food = models.ForeignKey(Food)


from your_app.models import Food, Person

my_favorite_food = Food.objects.create(name="Hamburgers", spicy=True)
joel = Person.objects.create(name="Joel", favorite_food=my_favorite_food)

# Is Joel's favorite food spicy?
print(joel.favorite_food.spicy)