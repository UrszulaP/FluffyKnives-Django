from django.urls import path
from . import views # . - obecna lokalizacja, import naszych widoków

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('about/', views.about, name='shop-about'),
] # (URL, widok, nazwa URL używana w templatkach)