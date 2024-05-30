from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import CommandStart

from menu import get_menu

r = Router()

@r.message(CommandStart())
async def h_start(message: Message):
    kb = await get_menu()

    await message.reply_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqV2LLzNbLJmSOuDJ-9VrVKSD6Xk3AP8szig&s",
        caption="current cryptocurrencies price in *USD*, data from [CoinMarketCap](https://coinmarketcap.com/)",
        reply_markup=kb)

@r.callback_query(F.data == 'rel')
async def h_reload(callback: CallbackQuery):
    kb = await get_menu()

    await callback.message.edit_reply_markup(reply_markup=kb)