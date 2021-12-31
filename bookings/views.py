from django.shortcuts import render
from django.views import generic, View
from django.views.generic.edit  import CreateView
from .models import Booking
from .forms import BookingForm


class BookTable(CreateView):
    model = Booking
    form_class = BookingForm
    queryset = Booking.objects.all()
    template_name = "bookings.html"

    def reserve_table(request):
        reserve_form = BookingForm()

        if request.method == 'POST':
            reserve_form = BookingForm(request.POST)

            if reserve_form.is_valid():
                reserve_form.save()
            else:
                reserve_form = BookingForm()
                
        return render(request, 'bookings.html', {'form': reserve_form})