import os
import openai
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = os.getenv("API_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_cmd_handler(message: types.Message):
    await message.answer("Hi! I'm a ChatGenie chatbot. Ask me anything!")


@dp.message_handler()
async def message_handler(message: types.Message):
    # Generate response using ChatGPT
    response = openai.Completion.create(
        engine='davinci',
        prompt=message.text,
        max_tokens=50
    )['choices'][0]['text']
    # Send response to user
    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
