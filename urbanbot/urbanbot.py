import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from api import api

api = api # api бота лижит в одельном файле что бы каждый раз не писать
bot = Bot(token=api)
dp = Dispatcher()

router = Router()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@router.message(Command("Calories"))
async def set_age(message: types.Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)


@router.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)


@router.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await state.set_state(UserState.weight)


@router.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
    await state.clear()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
