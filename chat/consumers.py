import json
from channels.generic.websocket import AsyncWebsocketConsumer
from myBot.bot import bot_response
from .chat import get_response, predict_class

"""Méthode de connexion asynchrone de base Il se connecte à l'appareil et 
effectue quelques étapes de préparation pour le travail"""

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group

            self.channel_name
        

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        #response = bot_response(message)
        ints=predict_class(message)
        #intents = json.loads(open('static/intents.json').read())
        with open('chat', 'r', encoding='') as file:
            intents = json.load(file)
        response = get_response(ints,intents)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'response': response
        }))
