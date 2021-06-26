from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', home, name='product_detail'),
]
