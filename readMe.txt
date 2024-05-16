pour créer un environnement: 
	1- python install pip
	2- python -m venv .env
	3- pip install --upgrade pip
	(.env/Scripts/activate)
	4- pip install django
	5- pip freeze > requirements.txt

pour créer un projet django:
	1- django-admin startproject mysite
	2- renommer de dossier "src"
	(cd src)
	3- Mise a jour de settings.py
		LANGUAGE_CODE = 'fr-FR'
		TIME_ZONE = 'Europe/Paris'
		MEDIA_ROOT = BASE_DIR/ "media"
		MEDIA_URL = '/media/'
		templates :
			'DIRS': [BASE_DIR / "templates"],

	3- python manage.py migrate

pour ajouter bootstrap:
	1- pip install django-bootstrap-v5
	2- dans la INSTALLED_APPS liste dans settings.py 
		'bootstrap5',
	3- ajouter ces liens au fichier html
		{% load bootstrap5 %}
	    {% bootstrap_css %}
	    {% bootstrap_javascript %}

pour ajouter une apli au projet :
	1- python manage.py startapp une_applie
	2- ajouter un dossier templates avec un sous-dossier au nom de l'applie
	2- ajouter un dossier static avec un sous-dossier au nom de l'applie + un dossier css / js / img
	3- ajouter un fichier urls.py


pour lancer le serveur de développement :
	1- rentrer dans le dossier du projet avec la commande : cd mon_projet
	2- python manage.py runserver  || python manage.py runserver 0.0.0.0:8000


pour gérer des images avec la db
1- Mettre sur le settings.py 
	# Définition du répertoire de stockage des fichiers média
	MEDIA_ROOT = BASE_DIR/ "media"

	# URL de base pour les fichiers média
	MEDIA_URL = '/media/'
2-Mettre a la suite de urlpatterns = [] dans urls.py du projet
	 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


pour créer une vue 
1- créer une fonction dans views.py
	def index(request):
		context = {
			"message" : "hello le monde",
		}
		return render(request, 'manga_lib/index.html', context)
2- créer le chemin dans urls.py
	app_name = "nom_de_lappli"
	urlpatterns = [
		path('', views.index, name='index'),
	]
3- enregistrer l'appli dans settings.py -> INSTALLED_APPS -> nom_de_lappli.apps.nom_de_lappliConfig
4- créer un chemin de urls.py du projet a urls.py de l'appli
	urlpatterns = [
		path('', include('manga_lib.urls')),
	]

pour réaliser des test (https://docs.python.org/3/library/unittest.html#module-unittest)
1- créer un class enfant de testcase
	class test_manga(TestCase)

2- créer une fonction pour créer les variable avec setUp
		def setUp(self):
			self.manga = Manga.objet.create(name= 'naruto')

3- créer des fonction test
		def test_is_instance(self)
			sef.assertIsInstance(self.manga, Manga)

3- python manage.py test     (--keepdb pour garder la bd-test)



pour appliquer des fichiers statique dans un fichier html (penser a relancer le server)
1-  {% load static %}
	<link rel="stylesheet" href="{% static 'nom_de_lapplie/css/style.css' %}">


pour créer des models (https://docs.djangoproject.com/fr/5.0/ref/models/fields/#django.db.models)
1- créer une classe
	class Manga(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField()
    comment = models.TextField()
    note =models.FloatField()
    origin = models.CharField(max_length=50)
    release_date = models.FloatField()

	def __str__(self):
        return self.title

2- python manage.py makemigrations
3- python manage.py migrate
4- dans le fichier admin.py
	from .models import Nom_du_model
    admin.site.register(Nom_du_model)

pour créer un admin
1- python manage.py createsuperuser
