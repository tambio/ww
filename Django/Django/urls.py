from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('main', views.main), 
    path('contact', views.contact),
    path('about', views.about),
]
 