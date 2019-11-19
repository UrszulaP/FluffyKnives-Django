from django.shortcuts import render
from .models import Item

def main(request):
    context = {
        'items_list': Item.objects.all()
    }
    return render(request, 'shop/main.html', context)
