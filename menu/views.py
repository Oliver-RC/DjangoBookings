from django.shortcuts import render
from django.views import generic
from .models import Menu


class MenuList(generic.ListView):
    model = Menu
    queryset = Menu.objects.filter(status=1)
    template_name = "menu.html"
    paginate_by = 8
