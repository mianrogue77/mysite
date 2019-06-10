from django.shortcuts import render
from django.utils.safestring import mark_safe

from config_game.models import Elemento

import json

# Create your views here.
def index(request):
    return render(request, 'chat/index.html', {})

# Vista room que redirecciona al template 'room.html'
def room(request, room_name):
    # Se optiene todos los registros del modelo 'Elemento'
    elements = Elemento.objects.all()
    # Envía información a la vista 'room'
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'elements': elements
    })
