from django.contrib import admin
from moviereviewapp.models import Rater
from moviereviewapp.models import Movie
from moviereviewapp.models import Review


# Register your models here.
admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Review)