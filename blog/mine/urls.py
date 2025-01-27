
from django.contrib import admin
from django.urls import path
from . import views

# localhost:8000/mine
# localhost:8000/mine/order
urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    # path('order/', views.order, name='order'),
]
