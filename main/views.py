from django.shortcuts import render

def page(request):
    return render(request, 'page.html')
from django.urls import path
from . import views

urlpatterns = [
    path('', views.page, name='page'),
]
