from django.urls import re_path

from . import consumers


websocket_urlpattterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer)
]