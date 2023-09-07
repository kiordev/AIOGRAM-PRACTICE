import asyncio # Импорт библиотеки ассинхронности
from aiogram import Bot, Dispatcher, F # импорт модулей
from aiogram.types import Message # Импорт message
from config import TOKEN_API

bot = Bot(token=TOKEN_API) # Присваевания API к токену
dp = Dispatcher()

@dp.message(F.text=='/my_id')
async def cmd_my_id(message: Message):
    await message.answer_photo(photo='https://twizz.ru/wp-content/uploads/2018/07/2rqlo3qgiv9vggpwibspndkfh4v50mngqzt2ghnlfo.jpg',
                               caption="Это пример отправки мемов") # Картинок

@dp.message()
async def echo(message: Message):
    await message.answer('Ничо не понял...')
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main()) # Функция для запуска бота


