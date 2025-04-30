# only collects urls from router/
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
]
