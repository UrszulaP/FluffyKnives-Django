from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='shop-main'),
] 