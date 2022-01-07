from django.shortcuts import render
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


def reserve_table(request):
    reserve_form = BookingForm(data=request.POST)

    if reserve_form.is_valid():
        reserve_form.save()
        messages.success(request, 'Success!')
        reserve_form = BookingForm()
    else: reserve_form = BookingForm()

    return render(request, 'bookings.html', {'form': reserve_form})