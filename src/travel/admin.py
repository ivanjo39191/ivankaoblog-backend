from django.contrib import admin

# Register your models here.
from .models import Travel, Rating, Place

admin.site.register(Travel)
admin.site.register(Rating)
admin.site.register(Place)