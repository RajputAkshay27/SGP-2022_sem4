from django.urls import path
from . import views

urlpatterns = [
   path('alloc',views.fac_alloc,name='Fac_alloc')
]