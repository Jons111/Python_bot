from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import base

viloyatlar = base.select_all_viloyatlar()
index = 0
keys = []
i = 0
for viloyat in (viloyatlar):
        nomi= viloyat[1]
        if i % 2 == 0 and i != 0:
            index += 1
        if i % 2 == 0:
            keys.append([KeyboardButton(text=f'{nomi}')])
        else:
            keys[index].append(KeyboardButton(text=f'{nomi}'))
        i += 1

taom_menu = ReplyKeyboardMarkup(keys, resize_keyboard=True
                                    )


viloyatlar_tugmalari = taom_menu

kontakt_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="kontakt",request_contact=True)
        ]
    ],
    resize_keyboard=True
)