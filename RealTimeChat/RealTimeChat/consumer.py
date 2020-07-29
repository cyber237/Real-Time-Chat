from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.consumer import AsyncConsumer
import datetime
from channels.layers import get_channel_layer

class Client(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self):
        self.channel_name=self.scope['id']
        self.channel_layer=get_channel_layer()
        await self.accept()
    
    async def receive_json(self,content):
        command=content["command"]
        if command=="message.send.private":
            await self.send_private(content["message"])
        elif command=="message.send.group":
            await self.send_group(content['message'])
    
    async def send_private(self,content):
        receiver=content['receiver']
        await self.channel_layer.send(
            receiver,
            {
            "type" : "chat.message",
            "receiver" :receiver,
            "message":content["message"],
            "date_sent":datetime.datetime.now()}
        )

    
    async def send_group(self,content):
        receiver=content['receiver']
        await self.channel_layer.group_send(
            receiver,
            {"type":"chat.message",
            "receiver":receiver,
            "message":content["message"],
            "date_sent":datetime.datetime.now()}
        )



        

        