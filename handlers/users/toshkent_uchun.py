from aiogram import types

from loader import dp
from keyboards.default.ob_havo import ob_havo_tugmasi
from keyboards.default.viloyatlar_buttons import viloyatlar_tugmalari
# Echo bot
@dp.message_handler(text='Toshkent')
async def bot_echo(message: types.Message):
    await message.answer(text='Kunini tanlang' ,reply_markup=ob_havo_tugmasi)


@dp.message_handler(text='Ortga')
async def bot_echo(message: types.Message):
    await message.answer(text='Kunini tanlang' ,reply_markup=viloyatlar_tugmalari)