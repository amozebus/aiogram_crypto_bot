import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from handling import r
from config import settings
from menu import update_currencies

bot = Bot(
    token=settings.TELEGRAM_BOT_API_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.MARKDOWN,
        link_preview_is_disabled=True
    )
)

dp = Dispatcher()
dp.include_router(r)

async def launch_bot(_logging: bool = False):
    await update_currencies()
    
    if _logging:
        logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot)