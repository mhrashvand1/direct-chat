import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from core import routers as chat_router
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket":AllowedHostsOriginValidator(
            SessionMiddlewareStack(
                AuthMiddlewareStack(
                    URLRouter(
                        chat_router.websocket_urlpatterns,
                    )
                )
            )
        )
    }
)