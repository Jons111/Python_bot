from aiogram import types
from googletrans import Translator
from loader import dp

tarjimon = Translator()
# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    til = tarjimon.detect(text=message.text).lang

    if til =='uz':
        matn = tarjimon.translate(text=message.text,dest='en' ,src='uz').text
        await message.answer(text=f'{matn}')
        matn = tarjimon.translate(text=message.text, dest='ru', src='uz').text
        await message.answer(text=f'{matn}')
    elif til=='en':
        matn = tarjimon.translate(text=message.text, dest='uz', src='en').text
        await message.answer(text=f'{matn}')
    else:
        matn = tarjimon.translate(text=message.text, dest='uz', src='en').text
        await message.answer(text=f'{matn}')
