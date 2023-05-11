from aiogram import types, Dispatcher
from config import bot


async def pin(message: types.Message):
    await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


async def echo(message: types.Message):
    if message.text.isdigit():
        message1 = int(message.text) ** 2
    else:
        await bot.send_message(message.chat.id, message.text)
        return
    await bot.send_message(message.chat.id, message1)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(echo)
