from django.contrib import admin

from .models import Rating


class RatingAdmin(admin.ModelAdmin):
    fields = ['rate', 'description', 'book']


admin.site.register(Rating, RatingAdmin)
