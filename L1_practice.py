from aiogram import executor, Dispatcher, Bot, types
from config import TOKEN_API # Перенос токена в отдельный файл

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
"""Задача: 
1) Выводить сообщение в верхнем регистре
2) Выводить его если сообщение состоит из более чем двух слов"""
@dp.message_handler()
async def echo(message: types.Message):
    if message.text.count(' ') >= 1:
            await message.answer(text=message.text.upper())
            