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
    path('primary_p/',views.primary_p,name="primary_p"),
    path('secondary_p/',views.secondary_p,name="secondary_p"),
    path('land_p/',views.land_p,name="land_p"),
    path('join_p/',views.join_p,name="join_p"),
    
    
]
