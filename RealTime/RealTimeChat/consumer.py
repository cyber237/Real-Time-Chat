from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.layers import channel_layers
import json
import datetime
from channels.layers import get_channel_layer
from data.model import Level 
from data.model import Student as stud
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async

class Students(AsyncJsonWebsocketConsumer):
    # class Client is our consumer for this connection
    # Tt manages the websocket connected to the server it also 
    # carries all methods we could apply to the connection

    async def websocket_connect(self,loop):
        # the websocket connect method is called any time
        # a connection is initiated to the server during handshake
        self.channel_layer=get_channel_layer()
        self.channel_name=str(self.scope['url_route']['kwargs']['id'])
        studObject= await database_sync_to_async(lambda : stud.objects.filter(id=self.channel_name)[0])()
        print(studObject)
        try:
            self.specialty= await database_sync_to_async(lambda:studObject.speciality)()
            self.level=await database_sync_to_async(lambda: studObject.level)()
        except:
            print("Failed")
        
        print(self.level)

        
        # Authentication Here
        await self.channel_layer.group_add("hnd",self.channel_name)
        await self.accept()

    
    async def receive_json(self,content):

        # This method is called anytime we recieve a packet from the connection
        command=content["type"]
        print(content)
        if command=="send.private":
            await self.send_private(content)
        elif command=="send.group":
            await self.send_group(content)
        elif command=="chat.receive":
            await self.chat_receive(content)
        elif command=="request.timetable":
            await self.getTimeTable()
        elif command=="update.timetable":
            await self.getTimeTable()

    
    async def send_private(self,content):
        # This method is called if the command of the packet received is a message to another user
        # we call it "private"
        receiver=content['receiver']

        await self.channel_layer.group_send(
            receiver,
            {
            "type" : "chat.receive",
            "receiver" :receiver,
            "message":content["message"]}
        )

    async def chat_receive(self,content):
        await self.send(
            text_data=json.dumps(content)
        )

    
    async def send_group(self,content):

        # This method is called any time the command in the packet is a group message

        receiver=content['receiver']
        await self.channel_layer.group_send(
            receiver,
            {"type":"chat.message",
            "receiver":receiver,
            "message":content["message"]}
        )

    async def fetch_timeTable(self,content):
        
        # This method is called anytime the command in the packet is a time table fetch command

        self.send(text_data=json.dumps({"timetable":"timetable"}))

    async def get_chats(self,user):
        # This method is to receive recent chats, and can be called by the web version,desktop
        # or mobile application to get chat of a specific user or group

        # This method should return a csv or database file to the user containing recent chats
        self.send(text_data="fetched data to binary")
    
    async def getTimeTable(self):
        levelObj=await database_sync_to_async(lambda: Level.objects.filter(speciality=self.specialty.id,level=self.level.level)[0])()
        print(levelObj)
        data=levelObj.timetable
        print("called")
        timetable=json.loads(data)
        
        if(len(timetable)<1):
            await self.channel_layer.group_send("hnd",{"type":"update.timetable","timetable":"n/a"})
        else:
            print("yeah")
            timetable=timetable[len(timetable)-1]
            respond={"type":"update.timetable","timetable":timetable}
            await self.send(json.dumps(respond))
            print("sent")
    

    

class Administrator(Students):
    async def websocket_connect(self,loop):
        # the websocket connect method is called any time
        # a connection is initiated to the server during handshake
        self.channel_layer=get_channel_layer()
        self.channel_name=str(self.scope['url_route']['kwargs']['id'])

    
        # Authentication Here
        await self.accept()
    async def receive_json(self,content):

        # This method is called anytime we recieve a packet from the connection
        command=content["type"]
        if command=="send.private":
            await self.send_private(content)
        elif command=="send.group":
            await self.send_group(content)
        elif command=="chat.receive":
            await self.chat_receive(content)
        elif command=="update.timetable":
            await self.sendTimeTable(content)


    async def sendTimeTable(self,content):
        specialty=content["specialty"]
        level=content["level"]
        timeTable=content["timetable"]

        newObject=await database_sync_to_async(lambda: Level.objects.filter(speciality=str(specialty),level=int(level))[0])()
        print(newObject)
        if(newObject):
            try:
                newObject.timetable=json.dumps([timeTable])
                await database_sync_to_async(lambda: newObject.save())()
            except:
                print("Failed")
        
        await self.channel_layer.group_send(
            "hnd",
            {"type":"update.timetable"}
        )
        print("sent")

        

        
    

        
   

        
