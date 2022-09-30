"""
ASGI config for myChatbot project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/

"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import chat.routing

"""
Channels fournit des classes de routage qui permettent de combiner et d'empiler les consommateurs 
(et toute autre application ASGI valide) à répartir en fonction de la connexion. On ne peut avoir qu'un 
seul consommateur pour une connexion donnée.

Channels prend en charge l'authentification Django standard prête à l'emploi pour les consommateurs 
HTTP et WebSocket
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '')

application = ProtocolTypeRouter({
  "websocket": AuthMiddlewareStack(
        URLRouter(
            
        )
    ),
})

"""
En plus de WSGI, Django prend également en charge le déploiement sur ASGI,
la norme Python émergente pour les serveurs et applications Web asynchrones.

Comme WSGI, ASGI demande de fournir une application appelable que le serveur d'application
utilise pour communiquer avec le code. Il est généralement fourni sous la forme d'un objet
nommé application dans un module Python accessible au serveur.

ASGI est la spécification du serveur sur laquelle le canal a été construit. Comme le WSGI, 
le serveur et le framework peuvent être choisis avec choix plutôt que d'accepter simplement le serveur Channel.

Le canal Django prend en charge HTTP et d'autres types de protocoles qui ont de longs temps de connexion. 
"""