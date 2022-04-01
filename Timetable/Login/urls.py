from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='LoginPage'),
    path('register',views.register , name='Registerpage'),
    path('home',views.index , name='Registerpage')
]