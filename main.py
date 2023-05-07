from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer(f'Добро пожаловать {message.from_user.full_name}')


@dp.message_handler(commands=["mem"])
async def mem_handler(message: types.Message):
    photo = open("coffee mem.png", "rb")
    await bot.send_photo(message.from_user.id, photo)


@dp.message_handler(commands=["quiz"])
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
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        reply_markup=markup
    )


@dp.callback_query_handler(text='button1')
async def quiz2(call: types.callback_query):
    question = "Какой самая популярная марка кофе?"
    answers = [
        "Starbucks",
        "Jardin",
        "Jockey",
        "Jacobs"
    ]

    markup = InlineKeyboardMarkup()
    button2 = InlineKeyboardButton("NEXT", callback_data="button2")
    markup.add(button2)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        reply_markup=markup
    )


@dp.callback_query_handler(text='button2')
async def quiz3(call: types.callback_query):
    await bot.send_message(call.from_user.id, "Quiz ended")


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        message1 = int(message.text) ** 2
    else:
        await bot.send_message(message.from_user.id, message.text)
        return
    await bot.send_message(message.from_user.id, message1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
