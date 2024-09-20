from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from api import api

api = api
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


button_calculate = KeyboardButton(text="Рассчитать")
button_info = KeyboardButton(text="Информация")

kb = ReplyKeyboardMarkup(
    keyboard=[[button_calculate], [button_info]],
    resize_keyboard=True
)

inline_kb = InlineKeyboardMarkup(row_width=2)
inline_kb.add(
    InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories'),
    InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text="Рассчитать")
async def main_menu(message: types.Message):
    await message.answer("Выбери опцию:", reply_markup=inline_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        "10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161"
    )
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if message.text == "Информация":
        await info_command(message, state)
        return

    try:
        await state.update_data(age=int(message.text))
        await message.answer("Введите свой рост:")
        await UserState.growth.set()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст.")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if message.text == "Информация":
        await info_command(message, state)
        return

    try:
        await state.update_data(growth=int(message.text))
        await message.answer("Введите свой вес:")
        await UserState.weight.set()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный рост.")


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    if message.text == "Информация":
        await info_command(message, state)
        return

    try:
        await state.update_data(weight=int(message.text))
        data = await state.get_data()

        age = data['age']
        growth = data['growth']
        weight = data['weight']
        calories = 10 * weight + 6.25 * growth - 5 * age + 5

        await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
    except ValueError:
        await message.answer("Пожалуйста, введите корректный вес.")


@dp.message_handler(lambda message: message.text == "Информация")
async def info_command(message: types.Message, state: FSMContext):
    await message.answer("Информация о боте.")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
