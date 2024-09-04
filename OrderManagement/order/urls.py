
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('final/',views.final,name='final'),
    path('delivery/',views.delivery,name='delivery'),
    path('order/',views.order,name='order'),
    
]
