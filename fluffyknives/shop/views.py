from django.shortcuts import render
from .models import Item

def main(request):
	context = {
		'itemsList': Item.objects.all()
	} #sposób wymagany przez Django, nie można bezpośrednio wczytać zmiennej
	# "Kontekst jest słownikiem mapującym nazwy zmiennych szablonu do obiektów Pythona."
	# context must be given as library type
	return render(request, 'shop/main.html', context)
