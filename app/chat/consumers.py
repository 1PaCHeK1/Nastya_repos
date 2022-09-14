import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from .models import (
    Chat,
    Message,
)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.room_id
        
        if isinstance(self.scope['user'], AnonymousUser):
            return await self.close(401)
        
        self.user = self.scope['user']
        chats = await sync_to_async(Chat.objects.filter)(id=self.room_id)
        if await sync_to_async(chats.exists)():
           self.chat = await sync_to_async(chats.first)()
        else:
            return await self.close(401)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )        
        await self.accept()
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': f"{self.user.username} in chat!"
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        if not isinstance(self.scope['user'], AnonymousUser):
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': f"Exiting a {self.user.username} from a chat!"
                }
            )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("WRITE MESSAGE")
        await sync_to_async(Message.objects.create)(
           owner=self.user,
           chat=self.chat,
           text=message
        )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    
    async def chat_message(self, event):
        message = event['message']
        print("READ MESSAGE")

        await self.send(text_data=json.dumps({
            'message': message
        }))