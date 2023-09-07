import asyncio # Импорт библиотеки ассинхронности
from aiogram import Bot, Dispatcher, F # импорт модулей
from aiogram.types import Message # Импорт message
from config import TOKEN_API

bot = Bot(token=TOKEN_API) # Присваевания API к токену
dp = Dispatcher()

@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!')
    
@dp.message(F.text == 'Саша')
async def sasha(message: Message):
    await message.reply('<b>Хуяшка</b>', parse_mode="HTML")

async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main()) # Функция для запуска бота
