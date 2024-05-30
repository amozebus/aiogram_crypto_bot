from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import settings
from cmc_api_client import CMCAPIClient

cmc_ids = {
    'btc': 1,
    'eth': 1027
}

def get_btn_text(cmc_id: int, quotes: dict):
    return f"{quotes[str(cmc_id)]['name']}: {round(quotes[str(cmc_id)]['quote']['USD']['price'], 2)}$"

async def get_menu():
    client = CMCAPIClient(api_key=settings.CMC_API_KEY)

    btc_data = await client.get_cc_quotes(cmc_ids['btc'])
    eth_data = await client.get_cc_quotes(cmc_ids['eth'])
    await client.close_session()

    kb = InlineKeyboardBuilder()
    kb.row(
        InlineKeyboardButton(text=get_btn_text(cmc_ids['btc'], btc_data), callback_data='btc')
    )
    kb.row(
        InlineKeyboardButton(text=get_btn_text(cmc_ids['eth'], eth_data), callback_data='eth')
    )
    kb.row(
        InlineKeyboardButton(text="Reload", callback_data='rel')
    )

    return kb.as_markup()