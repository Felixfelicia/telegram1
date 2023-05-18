import random
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, ADMINS
from database.bot_db import sql_command_delete, sql_command_all


async def game(message: types.Message):
    emojies = ("🎰", "🎲", "⚽", "🏀", "🎳", "🎯")
    random_emoji = random.choice(emojies)
    if message.chat.type != "private" and message.from_user.id in ADMINS:
        await bot.send_message(message.chat.id, random_emoji)
    else:
        await message.answer('Для игры необходимо написать "game"')


async def delete_data(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await message.answer(f"{user[1]}, {user[2]},"
                             f"{user[3]}, {user[4]}",
                             reply_markup=InlineKeyboardMarkup().add
                             (InlineKeyboardButton(f"Delete {user[3]}",
                                                   callback_data=f"delete {user[0]}")
                              ))


async def complete_delete(callback: types.CallbackQuery):
    await sql_command_delete(callback.data.split()[1])
    await callback.answer("Удалено!", show_alert=True)
    await callback.message.delete()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(
        complete_delete,
        lambda callback: callback.data and callback.data.startswith("delete ")
    )
