from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentType

from keyboards.default.viloyatlar_buttons import viloyatlar_tugmalari
from loader import dp, base, bot
from keyboards.inline.tillar_uchun import inline_tillar
from filters.shaxsiy_uchun import Shaxsiy
@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=inline_tillar)
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    user = message.from_user.username
    idd = message.from_user.id
    try:
        base.user_qoshish(ism=ism,tg_id=idd,fam=familya,username=user)
    except Exception as xatolik:
       pass
    await message.answer(f"Assalomu alaykum botga hush kelibsiz, {message.from_user.username}!")





@dp.message_handler(commands='reklama', chat_id = '1892438581')
async def bot_start(message: types.Message):
    users = base.select_all_foydalanuvchilar()

    for user in users:
            try:
                await bot.send_message(chat_id=user[4],text='Reklam yuborildi')

            except Exception as s:
                print(s)
                print(user)