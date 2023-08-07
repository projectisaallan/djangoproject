from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from sms1 import consumers

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/conversation/<int:user_id>/', consumers.ChatConsumer.as_asgi()),
    ]),
})