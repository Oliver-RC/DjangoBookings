from django.contrib import admin
from .models import Booking, Tables
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'table_size', 'date', 'time', 'requirements',)
    search_fields = ['email',]
    list_filter = ('date', 'time')
    summernote_fields = ('requirements',)


admin.site.register(Tables)