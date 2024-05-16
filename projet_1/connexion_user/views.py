from django.http import request
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


#page de connection 
def login_user(request):
	context = {
        'is_login_page': request.path.startswith("/login"),
		'message_error' : request.session.pop('message_error', None),
    }
    # si l'utilisateur est d�j� connect�
	if request.user.is_authenticated:
		return redirect('acceuil:acceuil')
        
	return render(request, 'connexion_user/login.html', context)

# verification du mot de passe et le nom d'utilisateur
def login_control(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)

		# si le mot de passe et le nom d'utilisateur sont bon
		if user is not None:
			login(request, user)
			return redirect('acceuil:acceuil')
            
		# si ils sont mauvais
		else:
			request.session['message_error'] = "erreur de saisie !!!"
			return redirect('connexion_user:login_acceuil')
		
	return render(request, 'connexion_user/login.html')

# page de deconnection
def logout_user(request):
	logout(request)
	return redirect('acceuil:acceuil')
		
#page de connection 
def add_user(request):	
	context = {
        'is_login_page': request.path.startswith("/login"),
		'message_error' : request.session.pop('message_error', None),
    }
	# si il est d�ja connecter
	if request.user.is_authenticated:
		return redirect('acceuil:acceuil')
		
	return render(request, 'connexion_user/add_user.html', context)

# verification des donnees pour inscription
def add_user_control(request):	
	# si il est d�ja connecter
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		password2 = request.POST["password2"]
		
		# verification si les 2 mot de passe sont identiques
		if password == password2 :
			user = authenticate(request, username=username, password=password)
			
			#verification que le nom n'est pas deja pris
			if not User.objects.filter(username=username).exists():
				user = User.objects.create_user(username=username, password=password)
				login(request, user)
				return redirect('acceuil:acceuil')

			#si le nom d'utilisateur est deja pris
			else:
				request.session['message_error'] = "le nom d'utilisateur est deja pris !!!"
				return redirect('connexion_user:add_user')
		
		# si les 2 mot de passe ne sont pas identiques
		else:
			request.session['message_error'] = "erreur de saisie !!!"
			return redirect('connexion_user:add_user')
            

		
	return redirect('connexion_user:add_user')