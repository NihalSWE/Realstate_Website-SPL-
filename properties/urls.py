from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),  # Updated path with trailing slash
    path('property/', views.property, name="property"),  # Updated path with trailing slash
    path('propertyAgent/',views.propertyAgent,name="propertyAgent"),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('career/', views.career, name='career'),
    
]
