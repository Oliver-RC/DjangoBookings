from django.contrib import admin
from .models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email',)
