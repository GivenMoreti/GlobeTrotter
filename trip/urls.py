from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.greet,name='greet'),
    path('trips/',views.get_trips,name="trips"),
    path('cars/',views.get_cars,name="cars"),
    path('users/',views.get_users,name="all-users"),
    path('request_trip/',views.request_trip,name="request-trip"),
    path ('cart/',views.cart,name="cart"),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/',views.register, name='register'),
    path('add_trip/',views.add_trip, name='add_trip'),
    path('add_car/',views.add_car, name='add_car'),
    path('edit_trip/<int:id>/', views.edit_trip, name='edit_trip'),
    path('delete/<int:id>/', views.deleted_trip, name='deleted_trip'),
    path('history/',views.history, name='history'),
    # path('activity/',views.recent_activity, name='recent_activity')
]
