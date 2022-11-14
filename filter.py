from aiogram.dispatcher.filters import Filter
from aiogram import types


class IsRightChat(Filter):
    """Фильтр для проверки источника сообщений."""
    key = "is_right_chat"

    async def check(self, message: types.Message):
        return message.chat.id == -780470984