from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Menu, Category


class MenuList(generic.ListView):
    model = Menu
    queryset = Menu.objects.filter(status=1)
    template_name = 'menu.html'
    extra_context = {'category_list': Category.objects.all()}


class MenuDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Menu.objects.filter(status=1)
        menu = get_object_or_404(queryset, slug=slug)

        return render(request, 'menu_detail.html', {"menu": menu})