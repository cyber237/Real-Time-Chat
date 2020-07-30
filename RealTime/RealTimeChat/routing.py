from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from . import consumer


application=ProtocolTypeRouter({
    "websocket":AuthMiddlewareStack(
        URLRouter([
            url(r'/^(?P<room_name>\w+)/$',consumer.BaseClient)
        ])
    )
})