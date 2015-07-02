# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mov_rate', '0005_auto_20150702_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('user_id', models.IntegerField()),
                ('movie_id', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
