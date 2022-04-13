from django.urls import path
from . import views

urlpatterns = [
    path('timetable',views.index, name='TimeTable'),
]