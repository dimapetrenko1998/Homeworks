from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from api import api
from crud_functions import *
from button import *

api = api
bot = Bot(token=api)

dp = Dispatcher(bot, storage=MemoryStorage())

drop_products_table()
initiate_db()
populate_products()


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=start_kb)


@dp.message_handler(lambda message: message.text == "Регистрация")
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text

    if not is_included(username):
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя")


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = int(message.text)
    data = await state.get_data()
    username = data.get("username")
    email = data.get("email")

    add_user(username, email, age)
    await message.answer("Регистрация завершена! Добро пожаловать!")
    await state.finish()


@dp.message_handler(lambda message: message.text == "Купить")
async def get_buying_list(message: types.Message):
    products = get_all_products()
    if not products:
        await message.answer("Нет доступных продуктов.")
        return

    for product in products:
        product_id, title, description, price, image_url = product
        product_description = f'Название: {title} | Описание: {description} | Цена: {price}'
        await message.answer(product_description)
        await bot.send_photo(message.chat.id, photo=image_url)


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Бот умеет считать калории, нажмите кнопку "Рассчитать"')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
            [InlineKeyboardButton(text='Формула расчета', callback_data='formulas')]
        ]
    ))


@dp.callback_query_handler(text="calories")
async def set_age(call: types.CallbackQuery):
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
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('''
    Рассчет калорий производится по формуле Миффлина-Сан Жеора

    Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161

    Для мужчин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) + 5
    ''')


if __name__ == "__main__":
    initiate_db()
    check_tables()
    executor.start_polling(dp, skip_updates=True)
