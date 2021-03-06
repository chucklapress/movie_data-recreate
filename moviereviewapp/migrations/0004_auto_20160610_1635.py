# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 16:35
from __future__ import unicode_literals

from django.db import migrations
import csv


def datareview(apps, schema_editor):
    Rater = apps.get_model('moviereviewapp', 'Rater')
    Movie = apps.get_model('moviereviewapp', 'Movie')
    Review = apps.get_model('moviereviewapp', 'Review')
    with open('/Users/chucklapress/tiy-projects/movie_data/ml-100k/u.data', 'r') as inFile:
        data = csv.reader(inFile, delimiter='\t')
        for row in data:
            temp_rater = Rater.objects.get(id=row[0])
            temp_movie = Movie.objects.get(id=row[0])
            Review.objects.create(rater=temp_rater, movie=temp_movie, rating=row[2], timestamp=row[3])




class Migration(migrations.Migration):

    dependencies = [
        ('moviereviewapp', '0003_auto_20160610_1628'),
    ]

    operations = [
        migrations.RunPython(datareview)
    ]
