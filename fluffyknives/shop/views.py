from django.shortcuts import render

itemsList = [
	{
		'itemImage': 'noz1.jpg',
		'itemName': 'Nóż 1',
		'itemMainDescription': 'Klasyka i elegancja, wszechstronność zastosowania, wykute w jednym nożu.',
		'itemPointsDescription': 'Klasyka i elegancja, wszechstronność zastosowania, wykute w jednym nożu.',
		'itemPrice': '299'
	},
	{
		'itemImage': 'noz1.jpg',
		'itemName': 'Nóż 1',
		'itemMainDescription': 'Klasyka i elegancja, wszechstronność zastosowania, wykute w jednym nożu.',
		'itemPointsDescription': 'Klasyka i elegancja, wszechstronność zastosowania, wykute w jednym nożu.',
		'itemPrice': "299"
	},
	{
		'itemImage': 'noz1.jpg',
		'itemName': 'Nóż 1',
		'itemMainDescription': 'Klasyka i elegancja, wszechstronność zastosowania, wykute w jednym nożu.',
		'itemPointsDescription': 'Klasyka i elegancja, wszechstronność zastosowania, wykute w jednym nożu.',
		'itemPrice': "299"
	}
]


def main(request):
	context = {
		'itemsList': itemsList
	} #sposób wymagany przez Django, nie można bezpośrednio wczytać zmiennej
	# "Kontekst jest słownikiem mapującym nazwy zmiennych szablonu do obiektów Pythona."
	return render(request, 'shop/main.html', context)
