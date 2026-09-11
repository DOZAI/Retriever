#import modules
import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters.command import Command

#Загружаем переменные из .env и читаем их через os.getenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Логика aiogram
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#импорт роутеров
from Handlers.basic_handlers import text_router
from Handlers.command_handlers import command_router
from Handlers.media_handlers import media_router



# Запуск процесса поллинга новых апдейтов
async def main():
    #подключаем роутер к диспетчеру
    dp.include_router(command_router)
    dp.include_router(text_router)
    dp.include_router(media_router)

    # Удаляем вебхук и пропускаем накопившиеся входящие сообщения
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
