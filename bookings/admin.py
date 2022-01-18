from django.contrib import admin
from .models import Booking, Tables
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'user', 'table_size', 'date', 'time', 'requirements', 'status',)
    search_fields = ['email', 'user',]
    list_filter = ('date', 'time', 'status', 'user',)
    summernote_fields = ('requirements',)


admin.site.register(Tables)