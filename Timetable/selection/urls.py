from django.urls import path
from . import views

urlpatterns = [
    path('priority', views.selection, name='Selectionpage')
]