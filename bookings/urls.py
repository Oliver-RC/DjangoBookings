from . import views
from django.urls import path

urlpatterns = [
    path('', views.reserve_table, name='bookings'),
    path('user-bookings/', views.table_reservations, name='user_bookings'),
]
