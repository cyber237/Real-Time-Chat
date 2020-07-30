from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.consumer import AsyncConsumer
import json
import datetime
from channels.layers import get_channel_layer

class BaseClient(AsyncJsonWebsocketConsumer):
    # class Client is our consumer for this connection
    # Tt manages the websocket connected to the server it also 
    # carries all methods we could apply to the connection

    async def websocket_connect(self):
        # the websocket connect method is called any time
        # a connection is initiated to the server during handshake
        self.channel_name=self.scope['url_route']['kwargs']['id']
        self.channel_layer=get_channel_layer()
        # Authentication Here
        self.channel_layer.group_add()
        await self.accept()
    
    async def receive_json(self,content):

        # This method is called anytime we recieve a packet from the connection

        command=content["type"]
        if command=="send.private":
            await self.send_private(content["message"])
        elif command=="send.group":
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

    async def fetch_timeTable(self,content):
        
        # This method is called anytime the command in the packet is a time table fetch command

        self.send(text_data=json.dumps({"timetable":"timetable"}))

    async def get_chats(self,user):
        # This method is to receive recent chats, and can be called by the web version,desktop
        # or mobile application to get chat of a specific user or group

        # This method should return a csv or database file to the user containing recent chats
        self.send(text_data="fetched data to binary")




        

        