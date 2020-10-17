from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from . import consumer


application=ProtocolTypeRouter({
    "websocket":AuthMiddlewareStack(
        URLRouter([
            url(r'(?P<id>\w+)/timeTable/$',consumer.Students),
            url(r'(?P<id>\w+)/timeTable/admin/$',consumer.Administrator),
        ])
    )
})