from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API
import random

list = ["A", "B", "C", "D"]

# bot = Bot(TOKEN_API)
# dp=Dispatcher(bot)

description = """
Создатель: Карай
Бот создан на AIOGRAM + PYTHON
Дата создания 01.09.2023
"""

@dp.message_handler(commands=['description'])
async def desc(message: types.Message):
    await message.answer(text=description)
    
counter = 0
@dp.message_handler(commands=['count'])
async def count(message: types.Message):
    global counter
    await message.answer(text=counter)
    counter = counter + 1
    
@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        await message.answer(text="YES")
    else:
        await message.reply("NO")
    
@dp.message_handler()
async def alphabet(message: types.Message):
    number = random.randint(0,3)
    await message.answer(text=list[number])