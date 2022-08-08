from aiogram import types
from aiogram.types import InputFile
from keyboards.inline.tillar_uchun import inline_tillar
from loader import dp,bot


# Echo bot
@dp.message_handler(text='Bugun')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzil = 'https://t.me/JoshDeveloper/1163'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,caption="""bugun havo <a href="https://t.me/ob_havo34_bot">salqin</a> boladi""",reply_markup=inline_tillar)
