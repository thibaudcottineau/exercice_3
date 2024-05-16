from django.urls import include, path
from . import views

app_name = "connexion_user"

urlpatterns = [
	path('', views.login_user, name='login_acceuil'),
    path('login', views.login_control, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('add_user', views.add_user, name='add_user'),
    path('add_user_control', views.add_user_control, name='add_user_control'),
]
