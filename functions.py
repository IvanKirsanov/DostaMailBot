from aiogram import types
from typing import List


def search_chat_id(msg_text: str, dep_id: dict) -> int:
    temp = msg_text.lower().split('\n')[:4]  # берём первые 4 абзаца сообщения и переводим в нижний регистр
    for chat_id, dep in dep_id.items():
        for values in dep:
            for line in temp:
                if values in line:
                    return values  # !!! исправить на chat_id
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
