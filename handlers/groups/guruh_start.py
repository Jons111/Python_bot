from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentType

from keyboards.default.viloyatlar_buttons import viloyatlar_tugmalari
from loader import dp,bot
from keyboards.inline.tillar_uchun import inline_tillar
from filters.guruh_uchun import Guruh
@dp.message_handler(Guruh(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"guruhga hush kelibsiz {message.from_user.full_name}!")


@dp.message_handler(Guruh(),content_types=ContentType.NEW_CHAT_MEMBERS)
async def bot_start(message: types.Message):
    await message.answer(f"guruhga hush kelibsiz {message.from_user.full_name}!")

@dp.message_handler(Guruh(),text='salom')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    await bot.kick_chat_member(chat_id='@sinov123450',user_id=user_id)