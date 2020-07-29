from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from consumer import Client


application=ProtocolTypeRouter({
    "websocket":AuthMiddlewareStack(
        URLRouter([
            url(r'^(?P<room_name>\w+)/$',Client)
        ])
    )
})