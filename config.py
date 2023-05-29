from decouple import config
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")
CHATAPI = config("CHATAPI")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

ADMINS = (6231235387, 5150075707)
