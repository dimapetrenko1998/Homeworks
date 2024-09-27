from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from api import api

api = api
bot = Bot(token=api)

dp = Dispatcher(bot, storage=MemoryStorage())

# Главная клавиатура
start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text="Информация"),
            KeyboardButton(text="Купить")  # Добавлена кнопка "Купить"
        ]
    ], resize_keyboard=True
)

# Inline клавиатура для выбора продуктов в ряд
inline_keyboard = InlineKeyboardMarkup(row_width=4)  # Устанавливаем ширину строки
for i in range(1, 5):
    button = InlineKeyboardButton(text=f"Product{i}", callback_data="product_buying")
    inline_keyboard.add(button)

# Клавиатура для расчета калорий
next_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формула расчета', callback_data='formulas')]
    ]
)


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(lambda message: message.text == "Купить")
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        product_description = f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}'
        await message.answer(product_description)  # Отправляем описание продукта
        await bot.send_photo(message.chat.id,
                             photo='https://cdn5.imgbb.ru/user/36/369623/201405/a00fc3d46d90c2dbfc5745e95bc893c3.jpg')

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda call: call.data == "product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.answer("Вы успешно приобрели продукт!")
    await bot.send_message(call.from_user.id, "Вы успешно приобрели продукт!")


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=start_kb)


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Бот умеет считать калории, нажмите кнопку "Рассчитать"')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=next_kb)


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_sex(message, state):
    await state.update_data(age=message.text)
    await message.answer("Укажите свой пол(м или ж):")
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)
async def set_growth(message, state):
    await state.update_data(sex=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = float(data['growth'])
    weight = float(data['weight'])
    sex = data.get('sex').lower()
    if sex == 'м':
        calories = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    elif sex == 'ж':
        calories = (10 * weight) + (6.25 * growth) - (5 * age) - 161
    else:
        await message.answer('Некоректно указан пол, пожалуйста, повторите попытку!')
        return
    await message.answer(f'Ваша норма калорий: {calories} ккал')
    await state.finish()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('''
    Рассчет калорий производится по формуле Миффлина-Сан Жеора

    Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161

    Для мужчин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) + 5
    ''')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
