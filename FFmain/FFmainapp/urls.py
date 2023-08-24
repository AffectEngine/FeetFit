from django.urls import path
from . import views

app_name = 'FFmainapp'  # Set the app namespace (if desired)

urlpatterns = [
    path('', views.home, name='home'),
]
