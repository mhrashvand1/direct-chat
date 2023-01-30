from core import consumers
from django.urls import path

websocket_urlpatterns = [
    path(
        'ws/chat/', consumers.ChatConsumer.as_asgi(), name='chat'
    ),   
]