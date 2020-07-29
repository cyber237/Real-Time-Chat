from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.consumer import AsyncConsumer
import datetime
from channels.layers import get_channel_layer

class Client(AsyncJsonWebsocketConsumer):
    # class Client is our consumer for this connection
    # Tt manages the websocket connected to the server it also 
    # carries all methods we could apply to the connection

    async def websocket_connect(self):
        # the websocket connect method is called any time
        # a connection is initiated to the server during handshake

        self.channel_name=self.scope['id']
        self.channel_layer=get_channel_layer()
        await self.accept()
    
    async def receive_json(self,content):

        # This method is called anytime we recieve a packet from the connection

        command=content["command"]
        if command=="message.send.private":
            await self.send_private(content["message"])
        elif command=="message.send.group":
            await self.send_group(content['message'])
    
    async def send_private(self,content):
        # This method is called if the command of the packet received is a message to another user
        # we call it "private"
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

        # This method is called any time the command in the packet is a group message
        
        receiver=content['receiver']
        await self.channel_layer.group_send(
            receiver,
            {"type":"chat.message",
            "receiver":receiver,
            "message":content["message"],
            "date_sent":datetime.datetime.now()}
        )



        

        