#импорт модулей
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters.command import Command

#настройка командного роутера
command_router = Router()

# Хэндлер на команды
@command_router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.full_name}! Я эхо-бот. Отправь мне любое сообщение, и я его повторю.")
