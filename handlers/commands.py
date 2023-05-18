from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from .keyboards import start_markup
from database.bot_db import sql_command_random


async def start_handler(message: types.Message):
    await message.answer(f'Добро пожаловать {message.from_user.full_name}', reply_markup=start_markup)


async def mem_handler(message: types.Message):
    photo = open("coffee mem.png", "rb")
    await bot.send_photo(message.chat.id, photo)


async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("NEXT", callback_data="button1")
    markup.add(button1)
    question = "Какая страна считается родиной кофе?"
    answers = [
        "Бразилия",
        "Эфиопия",
        "Колумбия",
        "Вьетнам"
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        reply_markup=markup
    )


async def get_user(message: types.Message):
    user: tuple = await sql_command_random()
    await message.answer(f"{user[1]}, {user[2]}, "
                  f"{user[3]}, {user[4]}")


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(quiz1, commands=['quiz'])
    dp.register_message_handler(get_user, commands=['get'])
