from django.urls import path
from . import views

urlpatterns = [
    path('login',views.home, name='LoginPage'),
    path('register',views.register , name='Registerpage'),
    path('home',views.index , name='homepage'),
    path('logout',views.logout_user)
]