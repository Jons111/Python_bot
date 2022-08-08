from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

from loader import dp,bot
from states.holatlar import Forma
from keyboards.default.ob_havo import tasdiqlash
from keyboards.default.viloyatlar_buttons import kontakt_button
# Echo bot
@dp.message_handler(text='Murojaat')
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(text='Ismni kiriting')
    await Forma.ism_qabul_qilish_holati.set()


@dp.message_handler(state=Forma.ism_qabul_qilish_holati)
async def bot_echo(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data({'ismim':ism})
    await message.answer(text='Familya kiriting')
    await Forma.fam_qabul_qilish_holati.set()

@dp.message_handler(state=Forma.fam_qabul_qilish_holati)
async def bot_echo(message: types.Message,state:FSMContext):
    familya = message.text
    await state.update_data({'fam':familya})
    await message.answer(text='Yoshni kiriting')
    await Forma.yosh_qabul_qilish_holati.set()

@dp.message_handler(state=Forma.yosh_qabul_qilish_holati)
async def bot_echo(message: types.Message,state:FSMContext):
    y = message.text
    await state.update_data({'yosh':y})
    await message.answer(text='Telni kiriting',reply_markup=kontakt_button)
    await Forma.tel_qabul_qilish_holati.set()

@dp.message_handler(state=Forma.tel_qabul_qilish_holati,content_types=ContentType.CONTACT)
async def bot_echo(message: types.Message,state:FSMContext):
    t = message.text
    await state.update_data({'tel':t})
    await message.answer(text='Murojaatni kiriting')
    await Forma.murojaat_qabul_qilish_holati.set()
@dp.message_handler(state=Forma.tel_qabul_qilish_holati)
async def bot_echo(message: types.Message,state:FSMContext):
    t = message.text
    await state.update_data({'tel':t})
    await message.answer(text='Murojaatni kiriting')
    await Forma.murojaat_qabul_qilish_holati.set()

@dp.message_handler(state=Forma.murojaat_qabul_qilish_holati)
async def bot_echo(message: types.Message,state:FSMContext):
    m = message.text
    await state.update_data({'murojaat':m})
    malumotlarim = await state.get_data()
    ism = malumotlarim.get('ismim')
    fam = malumotlarim.get('fam')
    age = malumotlarim.get('yosh')
    tel = malumotlarim.get('tel')
    matn = malumotlarim.get('murojaat')

    www = f"Ism :{ism}\n" \
           f"Familya :{fam}\n" \
           f"Yosh :{age}\n" \
           f"No'mer :{tel}\n" \
           f"Murojaat :{matn}\n" \

    await message.answer(text=www,reply_markup=tasdiqlash)
    await Forma.tasdiqlash.set()


@dp.message_handler(state=Forma.tasdiqlash,text='Ha')
async def bot_echo(message: types.Message,state:FSMContext):
    user_id = message.from_user.id
    malumotlarim = await state.get_data()
    ism = malumotlarim.get('ismim')
    fam = malumotlarim.get('fam')
    age = malumotlarim.get('yosh')
    tel = malumotlarim.get('tel')
    matn = malumotlarim.get('murojaat')

    www = f"Ism :{ism}\n" \
          f"Familya :{fam}\n" \
          f"Yosh :{age}\n" \
          f"No'mer :{tel}\n" \
          f"Murojaat :{matn}\n"
    await bot.send_message(chat_id='1892438581',text=www)
    await bot.send_message(chat_id=user_id,text="Adminga yuborildi")
    await state.finish()

@dp.message_handler(state=Forma.tasdiqlash,text="Yo'q")
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(text="Bekor qilindi")
    await state.finish()