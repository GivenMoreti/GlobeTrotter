from django.contrib import admin

# Register your models here.
from .models import Car,Trip,Cart,UserProfile

class CarModel(admin.ModelAdmin):
    list_display = ("make","model","driver","year")

class TripModel(admin.ModelAdmin):
    list_display = ("start_location","end_location","distance","car","user","status","seats_avail")
class UserProfileModel(admin.ModelAdmin):
    list_display = ("user","is_driver")

admin.site.register(Car,CarModel)
admin.site.register(Trip,TripModel)
admin.site.register(Cart)
admin.site.register(UserProfile,UserProfileModel)