import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

#Загружаем переменные из .env
load_dotenv()

# 2. Читаем их через os.getenv
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.full_name}! Я эхо-бот. Отправь мне любое сообщение, и я его повторю.")
# Хэндлер на остальные текстовые сообщения
@dp.message()
async def echo_handler(message: types.Message):
    text = message.text
    if text == f"My name is {message.from_user.full_name}":
        await message.answer(f"Hello {message.from_user.full_name}")
    elif text == "cat":
        await message.answer("You sent 'cat'! Here's a cat for you: 🐱")
    else:
        await message.answer(f"Я получил твое сообщение: {text}")

# Запуск процесса поллинга новых апдейтов
async def main():
    # Удаляем вебхук и пропускаем накопившиеся входящие сообщения
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
