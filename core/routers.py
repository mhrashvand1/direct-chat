from core import consumers
from django.urls import path

websocket_urlpatterns = [
    path(
        'chat/', consumers.ChatConsumer.as_asgi(), name='chat'
    ),   
]