# chat/routing.py
from django.urls import re_path

from .consumers import ChatConsumer

# Define la ruta de conexion para el consumidor
websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer),
]