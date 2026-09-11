#импорт модулей
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters.command import Command

#настройка текстового роутера
text_router = Router()


# Хэндлер на текстовые сообщения
@text_router.message(F.text)
async def echo_handler(message: types.Message):
    text = message.text
    if text == f"My name is {message.from_user.full_name}":
        await message.answer(f"Hello {message.from_user.full_name}")
    elif text == "cat":
        await message.answer("You sent 'cat'! Here's a cat for you: 🐱")
    else:
        await message.answer(f"Я получил твое сообщение: {text}")

