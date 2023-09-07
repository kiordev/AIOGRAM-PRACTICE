# Imports
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from config import TOKEN_API

bot = Bot(token=TOKEN_API)
dp = Dispatcher()

@dp.message(F.text == '/send_image')
async def cmd_send_image(message: Message):
    await message.answer_photo(photo="https://s00.yaplakal.com/pics/pics_original/5/3/4/9823435.jpg",
                               caption="Прикол, да?")


async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())



    