# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from config_game.models import Elemento, Efecto

import json

# Consumidor del canal
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # Obtiene la información que se han suministrados los jugadores
        element_one = text_data_json['element_one']
        element_two = text_data_json['element_two']

        word_key = ''

        # Valida si los jugadores han seleccionado algún elemetno
        if (len(element_one) > 0) and (len(element_two) > 0):
            # Consulta la configuración de los elementos seleccionados por los jugadores
            my_element_one = Elemento.objects.filter(nombre__contains=element_one)
            my_element_two = Elemento.objects.filter(nombre__contains=element_two)
            my_efect = Efecto.objects.filter(element_one__in=my_element_one, element_two__in=my_element_two)

            if len(my_efect) == 0:
                element_temp = element_one
                element_one = element_two
                element_two = element_temp

                my_efect = Efecto.objects.filter(element_one__in=my_element_two, element_two__in=my_element_one)
            
            # Se establece el efecto que tiene un elemento del otro
            word_key = my_efect[0].key_word

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'element_one': element_one,
                'element_two': element_two,
                'word_key': word_key
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        element_one = event['element_one']
        element_two = event['element_two']
        word_key = event['word_key']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'element_one': element_one,
            'element_two': element_two,
            'word_key': word_key
        }))