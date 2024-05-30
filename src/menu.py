from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message, InlineKeyboardButton, InputMediaPhoto

from config import settings
from cmc_api_client import CMCAPIClient
from currency import currencies, rounded, update_currencies

caption="current cryptocurrencies price in *USD*(data from [CoinMarketCap](https://coinmarketcap.com/))\n"\
"to get percentage price changing in periods tap to choosed currency button"
image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqV2LLzNbLJmSOuDJ-9VrVKSD6Xk3AP8szig&s"

async def menu(message: Message, reload: bool = False, back: bool = False):
    client = CMCAPIClient(settings.CMC_API_KEY)
    
    if reload:
        await update_currencies()

    kb = InlineKeyboardBuilder()
    for currency in currencies:
        kb.row(
            InlineKeyboardButton(
                text=f"{currency.name}: {rounded(currency.quote['USD']['price'])}$",
                callback_data=currency.slug
            )
        )
    await client.close_session()

    kb.row(
        InlineKeyboardButton(
            text=f"Reload",
            callback_data='rel'
        )
    )

    if reload or back:
        await message.edit_media(
            media=InputMediaPhoto(
                media=image,
                caption=caption
            ),
            reply_markup=kb.as_markup()
        )
    else:
        await message.answer_photo(
            photo=image,
            caption=caption,
            reply_markup=kb.as_markup()
        )