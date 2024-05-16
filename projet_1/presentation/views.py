from django.shortcuts import render

from .classe.fizzBuzz import FizzBuzz

def index(request):
	obj_fizzbuzz = FizzBuzz(0, 101)
	
	context = {
		"list_numbers" : obj_fizzbuzz.add_total(),
	}
	return render(request, 'presentation/index.html', context)








	# creer un kata en suivant la video  https://www.youtube.com/watch?v=P9oyYr7uIDc