from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default.viloyatlar_buttons import viloyatlar_tugmalari
from loader import dp


# Echo bot
@dp.callback_query_handler(text='til1')
async def bot_echo(message: CallbackQuery):
    await message.message.answer(text='Viloyatni tanlang',reply_markup=viloyatlar_tugmalari)

