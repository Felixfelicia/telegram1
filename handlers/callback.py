from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


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


async def quiz3(call: types.callback_query):
    question = "В какой стране отмечается день кофе?"
    answers = [
        "США",
        "Англия",
        "Япония",
        "Турция"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2

    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, text='button1')
    dp.register_callback_query_handler(quiz3, text='button2')
