from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name='General'),
    path('about/', views.about, name='About'),
]