from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

"""
Une fonction de vue pour les vues basées sur les classes. Il peut également s'agir d'un django.urls.include(). 
Permet de passer des arguments supplémentaires à la fonction ou à la méthode de vue. Voir Passer des options 
supplémentaires pour afficher les fonctions. 

"""