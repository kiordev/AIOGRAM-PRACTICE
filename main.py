# Imports
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from config import TOKEN_API
from text import START_MESSAGE, COMMANDS_MESSAGE, INFO_MESSAGE

bot = Bot(token=TOKEN_API)
dp = Dispatcher()

# Команды
@dp.message(F.text=="/начать")
async def cmd_start(message: Message):
    await message.answer(START_MESSAGE, parse_mode="HTML")

@dp.message(F.text=="/команды")
async def cmd_start(message: Message):
    await message.answer(COMMANDS_MESSAGE, parse_mode="HTML")
    
@dp.message(F.text=="/инфо")
async def cmd_start(message: Message):
    await message.answer(INFO_MESSAGE, parse_mode="HTML")
    
@dp.message()
async def cmd_start(message: Message):
    await message.answer("Я ничего не понял))) напиши /команды")

async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())



    