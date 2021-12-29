from django.contrib import admin
from .models import Menu, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):
    list_display = ('meal_name', 'slug', 'category', 'vegetarian_vegan', 'status', 'created_on')
    search_fields = ['meal_name', 'description']
    list_filter = ('status', 'category', 'vegetarian_vegan', 'created_on')
    prepopulated_fields = {'slug': ('meal_name',)}
    summernote_fields = ('description',)

admin.site.register(Category)