import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Code, Group

online_users = {}

class CodeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        self.username = self.scope['user'].username  # Assumes user is authenticated

        self.group = await self.get_group(self.group_name)
        
        if self.group_name not in online_users:
            online_users[self.group_name] = []
        
        if self.username not in online_users[self.group_name]:
            online_users[self.group_name].append(self.username)

        self.latest_code = ""
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'user_list_update',
                'online_users': online_users[self.group_name],
            }
        )

        print(f'User {self.username} connected to group {self.group_name}')

    async def disconnect(self, close_code):
        if self.group_name in online_users and self.username in online_users[self.group_name]:
            online_users[self.group_name].remove(self.username)

            if not online_users[self.group_name]:
                del online_users[self.group_name]

        print(f"Saving the data {self.latest_code}")
        print(f"User {self.username} disconnected from group {self.group_name}")
        
        await self.save_code_to_db(self.group, self.latest_code)
        
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'user_list_update',
                'online_users': online_users.get(self.group_name, []),
            }
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        code = text_data_json.get('code', None)

        self.latest_code = code.replace('\r\n', '\n')

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'code_message',
                'code': code
            }
        )

    async def code_message(self, event):
        code = event['code']

        await self.send(text_data=json.dumps({
            'code': code
        }))

    async def user_list_update(self, event):
        await self.send(text_data=json.dumps({
            'online_users': event['online_users']
        }))

    @database_sync_to_async
    def get_group(self, group_name):
        return Group.objects.get(name=group_name)

    @database_sync_to_async
    def save_code_to_db(self, group, code):
        code_entry, created = Code.objects.update_or_create(group=group, defaults={'content': code})
        return code_entry
