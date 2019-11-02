from django.shortcuts import render
from .models import Item

def main(request):
    context = {
        'items_list': Item.objects.all()
    } # method required by Django, it is not possible to use variable directly
    # "Kontekst jest słownikiem mapującym nazwy zmiennych szablonu do obiektów Pythona."
    # context must be given as library type
    return render(request, 'shop/main.html', context)
