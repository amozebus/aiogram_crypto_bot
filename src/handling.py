from aiogram import Router, F
from aiogram.filters.command import CommandStart
from aiogram.types import Message, CallbackQuery

from menu import menu
from currency import currencies

r = Router()

@r.message(CommandStart())
async def h_start(message: Message):
    await menu(message)

@r.callback_query(F.data == 'bitcoin')
async def h_btc(callback: CallbackQuery):
    await currencies[0].periods_menu(callback.message)

@r.callback_query(F.data == 'ethereum')
async def h_eth(callback: CallbackQuery):
    await currencies[1].periods_menu(callback.message)

@r.callback_query(F.data == 'back')
async def h_reload(callback: CallbackQuery):
    await menu(callback.message, back=True)

@r.callback_query(F.data == 'rel')
async def h_reload(callback: CallbackQuery):
    await menu(callback.message, reload=True)