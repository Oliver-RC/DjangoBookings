from . import views
from django.urls import path

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
]
