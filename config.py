from decouple import config
from aiogram import Dispatcher, Bot


TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot)

ADMINS = (6231235387, 6193417605)
