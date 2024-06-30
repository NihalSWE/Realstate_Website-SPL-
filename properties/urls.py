from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),  # Updated path with trailing slash
    path('property/', views.property, name="property"),  # Updated path with trailing slash
    path('propertyAgent/',views.propertyAgent,name="propertyAgent"),
    # path('property/', views.property_list, name='property_list'),
    
    
]
