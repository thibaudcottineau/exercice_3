from django.shortcuts import render

def index(request):
		context = {
			"message" : "hello le monde",
		}
		return render(request, 'presentation/index.html', context)
