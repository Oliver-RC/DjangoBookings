from . import views
from django.urls import path

urlpatterns = [
    path('', views.MenuList.as_view(), name='menu'),
    path('<slug:slug>/', views.MenuDetail.as_view(), name='menu_detail'),
]
