from __future__ import unicode_literals

from django.db import models, migrations

from mov_rate.models import Movie

from csv import reader

def create_movie_data(x, y):
    with open("ml-latest-small/movies.csv") as infile:
        comma_fix = list(reader(infile))
        for movie in comma_fix[1:]:
            movie_list = movie #.replace("\n", "").split(',')
            genre_list = movie_list.pop().split('|')
            d = {_.lower().replace("-", "_"): True for _ in genre_list}
            Movie.objects.create(movie_id = movie_list[0], id=movie_list[0], title=movie_list[1], **d)


class Migration(migrations.Migration):

    dependencies = [
        ('mov_rate', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_movie_data)
    ]
