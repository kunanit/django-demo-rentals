from django.contrib import admin
from rentals.models import Trip, Vehicle, User

# Register your models here.
admin.site.register(Trip)
admin.site.register(Vehicle)
admin.site.register(User)