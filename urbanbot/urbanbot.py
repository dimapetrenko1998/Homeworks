import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import Router

api = ''

bot = Bot(token=api)
dp = Dispatcher()

router = Router()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')


@dp.message()
async def all_messages(message: types.Message):
    await message.answer((message.text))


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
