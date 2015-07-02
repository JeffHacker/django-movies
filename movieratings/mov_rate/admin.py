from django.contrib import admin

# Register your models here.
from mov_rate.models import Movie
from mov_rate.models import Rating

admin.site.register(Movie)
admin.site.register(Rating)