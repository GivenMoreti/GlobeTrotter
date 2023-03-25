from django.contrib import admin

# Register your models here.
from .models import Car,Trip,Cart

class CarModel(admin.ModelAdmin):
    list_display = ("make","model","driver","year")

class TripModel(admin.ModelAdmin):
    list_display = ("start_location","end_location","distance","car","driver","status","seats_avail")


admin.site.register(Car,CarModel)
admin.site.register(Trip,TripModel)
admin.site.register(Cart)