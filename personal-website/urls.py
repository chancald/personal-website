from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('', include('home.urls')),
    path('', include('masks.urls'))
]
