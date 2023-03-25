from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render, redirect
from .models import Trip, Cart,Car
from .forms import TripRequestForm,TripForm,CarForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from datetime import datetime

from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType

@login_required
def request_trip(request):
    if request.method == 'POST':
        form = TripRequestForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()
            cart, created = Cart.objects.get_or_create(owner=request.user)
            cart.trips.add(trip)
            return redirect('cart')
    else:
        form= TripRequestForm()
    return render(request, 'trip/request_trip.html',{"form":form})

# add a trip once logged in
@login_required
def add_trip(request):
    if request.method == 'POST':
        add_trip_form = TripForm(request.POST)
        if add_trip_form.is_valid():
            trip = add_trip_form.save(commit=False)
            trip.trip_date = datetime.now() # replace with the actual trip date
            trip.status = 'Active'
            trip.save()

            # content_type = ContentType.objects.get_for_model(Trip)
            # LogEntry.objects.log_action(
            #     user_id=request.user.id,
            #     content_type_id=content_type.id,
            #     object_id=trip.id,
            #     object_repr=trip.driver,
            #     action_flag=ADDITION,
            #     change_message='Added a new trip'
            # )
            return redirect('trips')
    else:
        add_trip_form = TripForm()
    return render(request, 'trip/add_trip.html', {'add_trip_form': add_trip_form})

# allow logged in users to edit trips
def edit_trip(request, id):
    trip = Trip.objects.get(id=id)
    form = TripForm(instance = trip) 

    if request.method == 'POST':
        form = TripForm(request.POST,instance=trip)
        if form.is_valid():  
            form.save()  
            return redirect("trips")
    
    completed_trips = Trip.objects.filter(status='Completed')
    for ct in completed_trips:
        print("completed trips",ct.id)
        print("actions :",ct.driver,ct.trip_date)
    count_completed_trips = completed_trips.count()   
    
    
    
    return render(request, 'trip/edit_trip.html', {'form': form,
                                                   "count_completed_trips":count_completed_trips})

# working on all the users
@login_required
# homepage
def get_users(request):
    all_users = User.objects.all()
    # for user in all_users:
    #     print(user.username)
    users_count = all_users.count()
    context = {"all_users":all_users,}
    return render (request,'trip/home.html',context)

# get all items in a cart
@login_required
def cart(request):
    cart_items = Cart.objects.all()
    context = {"cart_items":cart_items}
    return render(request,"trip/cart.html",context)

# get all trips
def get_trips(request):
    trips = Trip.objects.all()
    completed_trips = Trip.objects.filter(status='Completed')
    for completed_trip in completed_trips:
        print("completed trips",completed_trip.id)
        print(f"driver: {completed_trip.driver}, date : {completed_trip.trip_date}")
    
    count_completed_trips = completed_trips.count() 

    all_users = User.objects.all()
    users_count = all_users.count()

    cars = Car.objects.all()
    cars_count = cars.count() 
    # count all the requested trips 
    requested_trips = Trip.objects.filter(status="Requested")
    
    for requested_trip in requested_trips:
        print(f"requested trips {requested_trip.id}")
    count_requested_trips = requested_trips.count()
# count the active trips
    active_trips = Trip.objects.filter(status="Active")
    
    for active_trip in active_trips:
        print("Active trips:",active_trip.id)
    count_active_trips = active_trips.count()


    context = {
        "count_active_trips ":count_active_trips, 
            "count_requested_trips":count_requested_trips,
               "trips":trips,
               "count_completed_trips":count_completed_trips,
               "users_count":users_count,
               "cars":cars,"cars_count":cars_count
               }
    
    return render(request,"trip/home.html",context)


# login and logout a user
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('trips')
        else:
            return render(request, 'trip/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'trip/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('trips')


# register a user

from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trips')
    else:
        form = RegistrationForm()
    return render(request, 'trip/register.html', {'form': form})

# protecting the deleted trips in the database
from django.shortcuts import get_object_or_404
from .models import DeletedTrip

def deleted_trip(request, id):
    deleted_trip = get_object_or_404(Trip, pk=id)
    deleted_trip = DeletedTrip(name=deleted_trip.driver)
    deleted_trip.save()
    deleted_trip.delete()
    return redirect('trips')

def history(request):
    deleted_trips = DeletedTrip.objects.all().order_by('-deleted_at')
    return render(request,'trip/history.html',{"deleted_trips":deleted_trips})


# user can add a car
@login_required
def add_car(request):
    context ={}
    form = CarForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('cars')  
        
    context['form'] = form

    return render(request,'trip/add_car.html',context) 


# get all cars on the system
def get_cars(request):
    cars = Car.objects.all()
    cars_count = cars.count()
    context = {"cars":cars,"cars_count":cars_count}
    return render(request,"trip/cars.html",context)

# get user activity history
# from django.utils import timezone

# def recent_activity(request):
#     user = request.User
#     recent_activity = user.useractivity_set.filter(timestamp__gte=timezone.now()- timezone.timedelta(days=7))

#     return render( request,"trip/recent_activity.html",{"recent_activity":recent_activity})

