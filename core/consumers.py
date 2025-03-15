import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Code, Group

class CodeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']

        self.group = await self.get_group(self.group_name)
        
        self.latest_code = ""
        # Join the group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

        # Send a welcome message to the WebSocket
        print(f'Connected to group {self.group_name}')
      

    async def disconnect(self, close_code):
        print(f"Saving the data {self.latest_code}")
        print("The websocket is disconnected")
        await self.save_code_to_db(self.group, self.latest_code)
        # Leave the group when the WebSocket disconnects
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        code = text_data_json.get('code', None)

        # Save the code to the database asynchronously
        self.latest_code = code.replace('\r\n', '\n')

        # Broadcast the updated code to the group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'code_message',
                'code': code
            }
        )

    async def code_message(self, event):
        code = event['code']

        # Send the updated code to the WebSocket
        await self.send(text_data=json.dumps({
            'code': code
        }))

    @database_sync_to_async
    def get_group(self, group_name):
        return Group.objects.get(name =group_name)


    @database_sync_to_async
    def save_code_to_db(self, group, code):
        code_entry , created= Code.objects.update_or_create(group=group, content=code)
        return code_entry
