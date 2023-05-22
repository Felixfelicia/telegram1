from aiogram.utils import executor
import logging
import asyncio

from config import dp, bot, ADMINS
from handlers import commands, callback, admin, fsmAdminMentor, extra, notifications
from database.bot_db import sql_create


async def on_startup(dp):
    asyncio.create_task(notifications.set_scheduler())
    await bot.send_message(ADMINS[1], "Подключена!")
    sql_create()


async def on_shutdown(dp):
    await bot.send_message(ADMINS[1], "See you!")


commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsmAdminMentor.register_handlers_fsmAdminMentor(dp)

extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup,
                           on_shutdown=on_shutdown)
