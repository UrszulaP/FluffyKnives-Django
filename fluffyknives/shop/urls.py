from django.urls import path
from . import views # . - obecna lokalizacja, import naszych widoków

urlpatterns = [
    path('', views.main, name='shop-main'),
] # (URL, widok, nazwa URL używana w templatkach)
# nazwy muszą być unikalne, najlepiej z przedrostkiem nazwy aplikacji