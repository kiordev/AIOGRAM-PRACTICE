from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_): # Стартовая функция, срабатывает после запуска бота
    print("all is okey")
    
@dp.message_handler(commands=['start'])
async def starter(message: types.Message):
    await message.answer("<em>Привет, добро пожаловать!</em>", parse_mode="HTML")
    # parse_mod выставляет режим парсинга, как понимать сообщение.
    # в данном случае HTML - считывание разметки ХТМЛ, элементарной

@dp.message_handler(commands=['give'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEKOjxk9xfiWtkFkDOvthEXU-a9X6uEaAACph4AAg9GAAFKL_siv1E1IvwwBA")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)