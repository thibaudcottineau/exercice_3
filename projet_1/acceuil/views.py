from django.shortcuts import render

#page d'acceuil
def acceuil(request):
    context = {
		}
    return render(request, 'acceuil/acceuil.html', context)
