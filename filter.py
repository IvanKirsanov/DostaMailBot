from aiogram.dispatcher.filters import Filter
from aiogram import types
from config import source_chat_id


class IsSourceChat(Filter):
    """Фильтр для проверки источника сообщений."""
    key = "is_source_chat"

    async def check(self, message: types.Message):
        return message.chat.id == source_chat_id
