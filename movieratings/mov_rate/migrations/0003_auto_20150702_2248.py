# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from mov_rate.models import Rating, Movie

def create_rating_data(x, y):
    with open("ml-latest-small/ratings.csv") as infile:
        for rating in infile.readlines()[1:]:
            rating_list = rating.split(',')
            rating_list[0] = int(rating_list[0])
            rating_list[1] = int(rating_list[1])
            rating_list[2] = float(rating_list[2])
            Rating.objects.create(user_id=rating_list[0], rating=rating_list[2],
                                  movie_id = Movie.objects.get(movie_id=rating_list[1]))
            print(rating_list)

    #raise Exception()


class Migration(migrations.Migration):

    dependencies = [
        ('mov_rate', '0002_auto_20150702_1951'),
    ]

    operations = [
        migrations.RunPython(create_rating_data)
    ]
