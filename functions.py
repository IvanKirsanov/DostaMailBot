from aiogram import types
from typing import List
import re


def search_chat_id(msg_text: str, dep_id: dict) -> int:
    msg_text_lower = msg_text.lower().split('\n')[:4]  # берём первые 4 абзаца сообщения и переводим в нижний регистр
    for chat_id, dep_name in dep_id.items():
        for name in dep_name:
            for line in msg_text_lower:
                if re.search(pattern=name, string=line):
                    return name[2:-2]  # !!! исправить на chat_id
    return 0


def create_media_group(message: types.Message, album: List[types.Message], text: str) -> types.MediaGroup:
    media_group = types.MediaGroup()
    for obj in album:
        if obj.photo:
            file_id = obj.photo[-1].file_id
        else:
            file_id = obj[obj.content_type].file_id

        media_group.attach({"media": file_id, "type": obj.content_type,
                            "caption": text if album.index(obj) == 0 else ""})
                         # !!! "caption": message.caption if album.index(obj) == 0 else ""})
    return media_group
