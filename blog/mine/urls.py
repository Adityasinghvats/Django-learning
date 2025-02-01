
from django.contrib import admin
from django.urls import path
from . import views

# localhost:8000/mine
# localhost:8000/mine/order
urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('chai_stores/', views.chai_stores, name='chai_stores'),
    # path('order/', views.order, name='order'),
]
