import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Hi!\n"
        "I'm your first bot that you created!\n"
        "What's your name?'")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Nice to meet you!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
