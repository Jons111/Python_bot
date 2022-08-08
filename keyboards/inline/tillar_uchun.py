from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

inline_tillar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Uzb',callback_data='til1'),
            InlineKeyboardButton(text='Rus',callback_data='til2')
        ],
        [
            InlineKeyboardButton(text='Hamkorlarimiz',url='https://t.me/UstozShogird'),
            InlineKeyboardButton(text="Ulashish",switch_inline_query="Zo'r bot ekan ")
        ]
    ]
)
