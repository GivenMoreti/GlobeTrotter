from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from datetime import datetime
# Create your models here.
STATUS = (
    ("Active","Active"),
    ("Requested","Requested"),
    ("Completed","Completed")
)
# if the status is set to active- trip is available
# if the status is set to requested - trip is pending
# completed, trip should be deleted from the list 

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    driver = models.OneToOneField(User,on_delete=models.CASCADE)
    year = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add = True,null=True)
  
    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
    
    class Meta:
        ordering = ['-date_added']

class Trip(models.Model):
    
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='trips')
    # driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    # trip_date = models.DateTimeField(default=None,validators=[MinValueValidator(datetime.now)])
    trip_date = models.DateTimeField(datetime.now)
    # the user will change status to requested
    seats_avail= models.IntegerField(default=1)
    status = models.CharField(max_length=30,choices = STATUS,default="Active")
    # for database
    date_added = models.DateTimeField(auto_now_add = True,null=True)
  

    def __str__(self):
        return f"Trip from {self.start_location} to {self.end_location} ({self.distance} km)"
    
    
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'Trip {self.id}'
    
    
class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    trips = models.ManyToManyField('Trip', blank=True, related_name='carts')

    def __str__(self):
        return f"{self.owner}'s cart"

# for reference purposes,deleted and historical trips are saved on the system
class DeletedTrip(models.Model):
    deleted_trip = models.ForeignKey(Trip,on_delete=models.PROTECT)
    deleted_at = models.DateTimeField(auto_now_add=True)

# user profile to  modify default user
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=False)
    # user_image = models.CharField(max_length=8550)
    # rating = models.DecimalField(max_digits=3, decimal_places=2)


    def __str__(self):
        return self.user.username
    