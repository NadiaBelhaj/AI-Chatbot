"""
WSGI config for myChatbot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

"""
La plate-forme de déploiement principale de Django est WSGI.
Les serveurs WSGI obtiennent le chemin d'accès à l'application appelable à partir de leur configuration. 
Le serveur intégré de Django, à savoir la commande runserver, le lit à partir du paramètre WSGI_APPLICATION.
"""