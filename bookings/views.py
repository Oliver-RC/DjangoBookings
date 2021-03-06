from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


def reserve_table(request):
    reserve_form = BookingForm(data=request.POST)

    if reserve_form.is_valid():
        if request.user.is_authenticated:
            reserve_form.instance.user = request.user
            reserve_form.save()
            messages.success(request, 'Booking received!'
                             ' Please go to the "My Bookings"'
                             ' page to view your bookings and their status.')
            reserve_form = BookingForm()
        else:
            reserve_form.save()
            messages.success(request, 'Booking received! The restaurant will'
                             ' call to confirm your booking.')
            reserve_form = BookingForm()
    else:
        reserve_form = BookingForm()

    return render(request, 'bookings.html', {'form': reserve_form})


def table_reservations(request):
    reservations = Booking.objects.filter(user=request.user)

    return render(request, 'user_bookings.html',
                  {'reservations': reservations})


def update_reservation(request, pk):
    reserve = Booking.objects.get(id=pk)
    reserve_form = BookingForm(instance=reserve)

    if request.method == 'POST':
        reserve_form = BookingForm(request.POST, instance=reserve)
        if reserve_form.is_valid():
            reserve_form.save()
            return redirect('user_bookings')

    return render(request, 'bookings.html', {'form': reserve_form})


def delete_reservation(request, pk):
    reserve = Booking.objects.get(id=pk)

    if request.method == "POST":
        reserve.delete()
        return redirect('user_bookings')

    return render(request, 'delete.html', {'reserve': reserve})
