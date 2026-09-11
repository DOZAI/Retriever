#импорт модулей
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters.command import Command

#настройка командного роутера
media_router = Router()


# Хэндлер на команды
@media_router.message(F.audio)
async def cmd_start(message: types.Message):
    await message.answer(f"Классный музон!")

@media_router.message(F.sticker)
async def sticker_reply(message: types.Message):
    await message.answer("Классный стикер!")

@media_router.message(F.photo)
async def photo_reply(message: types.Message):
    await message.answer("Классное фото, но в следующий раз отправляй НЕ DickPic")