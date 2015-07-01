# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from mov_rate.models import Movie


def create_movie_data(x, y):
    with open("ml-latest-small/movies.csv") as infile:
        for movie in infile.readlines()[1:]:
            movie_list = movie.replace("\n", "").split(',')
            genre_list = movie_list.pop().split('|')
            d = {_.lower().replace("-", "_"): True for _ in genre_list}
            Movie.objects.create(id=movie_list[0], title=movie_list[1], **d)
    raise Exception()

class Migration(migrations.Migration):

    dependencies = [
        ('mov_rate', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_movie_data)
    ]
