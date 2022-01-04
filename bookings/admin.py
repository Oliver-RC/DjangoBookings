from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'number_of_guests', 'date', 'time', 'requirements',)
    search_fields = ['email',]
    list_filter = ('date', 'time')
    summernote_fields = ('requirements',)