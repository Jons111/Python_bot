from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

ob_havo_tugmasi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Bugun'),
            KeyboardButton(text='Ertaga'),

         ],
        [
            KeyboardButton(text='1haftadan keyin'),
            KeyboardButton(text="1oydan keyin")
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)

tasdiqlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ha'),
            KeyboardButton(text="Yo'q")
        ]
    ],
    resize_keyboard=True
)