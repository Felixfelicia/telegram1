import random
from aiogram import types, Dispatcher
from config import bot, ADMINS


async def game(message: types.Message):
    emojies = ("🎰", "🎲", "⚽", "🏀", "🎳", "🎯")
    random_emoji = random.choice(emojies)
    if message.chat.type != "private" and message.from_user.id in ADMINS:
        await bot.send_message(message.chat.id, random_emoji)
    else:
        await message.answer('Для игры необходимо написать "game"')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])
