from django.urls import re_path, path
from . import  consumers1

websocket_urlpatterns = [
    # re_path(r'ws/code/(?P<group_name>\w+)/$', consumers.CodeConsumer.as_asgi()),
    # path("ws/code/<str:group_name>/", consumers.CodeConsumer.as_asgi() )
    path("ws/code/<str:group_name>/", consumers1.CodeConsumer.as_asgi() )
]


