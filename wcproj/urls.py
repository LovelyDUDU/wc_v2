from django.contrib import admin
from django.urls import path
import wcapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wcapp.views.index, name="index"),
    path('result/', wcapp.views.result, name="result"),
]