import logging
from typing import List
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from middleware import AlbumMiddleware
from config import TOKEN, dep_chat_id
from functions import create_media_group, search_chat_id
from filter import IsRightChat

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


@dp.message_handler(IsRightChat(), content_types=[types.ContentType.PHOTO, types.ContentType.VIDEO,
                                   types.ContentType.DOCUMENT])
async def handle_albums(message: types.Message, album: List[types.Message]):
    msg_text = album[0].caption
    if not msg_text:
        await message.reply('Отсутствует текст сообщения')
        return True
    chat_id = search_chat_id(msg_text, dep_chat_id)
    if not chat_id:
        await message.reply('Департамент не указан, либо написан некорректно ❌')
        return 0
    media_group = create_media_group(message, album, str(chat_id))
    await message.answer_media_group(media_group)


if __name__ == '__main__':
    dp.middleware.setup(AlbumMiddleware())
    dp.bind_filter(IsRightChat)
    executor.start_polling(dp, skip_updates=True)
