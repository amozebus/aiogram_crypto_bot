from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message, InlineKeyboardButton, InputMediaPhoto

from config import settings
from cmc_api_client import CMCAPIClient

rounded = lambda x: round(x, 2)

periods_rows = [['1h', '24h'], ['7d', '30d']]

base_image = "https://s2.coinmarketcap.com/static/img/coins/128x128"
base_caption = "percentage price changing in periods of"

class BaseCurrency:
    def __init__(self, cmc_id: int):
        self.cmc_id = cmc_id

        self.data: dict = {}
        self.image: str
        self.caption: str
    
    def __getattr__(self, name: str):
        if name in self.data:
            return self.data[name]
        else: 
            raise AttributeError(name)

class Currency(BaseCurrency):
    async def update_data(self, client: CMCAPIClient):
        r_data = await client.get_data(
            path="/v2/cryptocurrency/quotes/latest",
            params={'id': self.cmc_id}
        )

        self.data = r_data[str(self.cmc_id)]
        self.image = f"{base_image}/{self.cmc_id}.png"
        self.caption = f"{base_caption} {self.name}"

    async def periods_menu(self, message: Message):
        kb = InlineKeyboardBuilder()
        kb.row(
            InlineKeyboardButton(text=f"Current price: {rounded(self.quote['USD']['price'])}$", callback_data='price')
        )
        for periods_row in periods_rows:
            row = []
            for period in periods_row:
                row.append(
                    InlineKeyboardButton(text=f"{period}: {rounded(self.quote['USD'][f'percent_change_{period}'])}%", callback_data=str(period))
                )
            kb.row(*row)
        kb.row(
            InlineKeyboardButton(text="Back", callback_data='back')
        )

        await message.edit_media(
            InputMediaPhoto(
                media=self.image,
                caption=self.caption
            ),
            reply_markup=kb.as_markup()
        )

currencies = [
    Currency(1), # bitcoin
    Currency(1027), # ethereum
    Currency(5426) # solana
]

async def update_currencies():
    client = CMCAPIClient(settings.CMC_API_KEY)
    for currency in currencies:
        await currency.update_data(client)
    await client.close_session()