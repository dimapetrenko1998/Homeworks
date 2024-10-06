from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text="Информация"),
            KeyboardButton(text="Купить"),
            KeyboardButton(text='Регистрация')
        ]
    ], resize_keyboard=True
)