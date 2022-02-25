from django.shortcuts import render

# Create your views here.

def selection(request):
    return render (request, 'selection/selection.html')
