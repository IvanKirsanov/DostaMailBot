import logging
from typing import List
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from middleware import AlbumMiddleware
from config import TOKEN, dep_chat_id
from functions import create_media_group, search_chat_id, find_caption
from filter import IsSourceChat

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


@dp.message_handler(IsSourceChat(), content_types=[types.ContentType.PHOTO, types.ContentType.VIDEO,
                                                   types.ContentType.DOCUMENT])
async def handle_albums(message: types.Message, album: List[types.Message]):
    msg_text = find_caption(album)
    if not msg_text:
        await message.reply('Не отправлено, отправьте сообщение еще раз (отсутствует текст сообщения) ❌')
        return True
    chat_id = search_chat_id(msg_text, dep_chat_id)
    if not chat_id:
        await message.reply(
            'Не отправлено, отправьте сообщение еще раз (департамент не указан, либо написан некорректно) ❌')
        return True
    media_group = create_media_group(album, caption=msg_text)
    await bot.send_media_group(chat_id, media_group)
    await message.reply('Отправлено ✅')


if __name__ == '__main__':
    dp.middleware.setup(AlbumMiddleware())
    dp.bind_filter(IsSourceChat)
    executor.start_polling(dp, skip_updates=False)
