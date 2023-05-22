import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from config import ADMINS

from config import bot


async def bday():
    await bot.send_message(ADMINS[1], "С днем рождения!")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")

    scheduler.add_job(
        bday,
        trigger=CronTrigger(
            month=6, day=3, hour=10, minute=5,
            start_date=datetime.datetime.now()
        )
    )

    scheduler.start()
