from aiogram import types
from aiogram.types import ContentType

from loader import dp


# Echo bot
@dp.message_handler(content_types=ContentType.DOCUMENT,chat_id='1892438581')
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text='Dacument qabul qilindi')

@dp.message_handler(content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message):
    await message.video.download()
    await message.answer(text='video qabul qilindi')

@dp.message_handler(content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[1].download()
    await message.photo[2].download()
    await message.answer(text='rasm qabul qilindi')