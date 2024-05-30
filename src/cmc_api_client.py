from aiohttp import ClientSession

class CMCAPIClient:
    def __init__(self, api_key: str):
        self._session = ClientSession(
            base_url="https://pro-api.coinmarketcap.com",
            headers={"X-CMC_PRO_API_KEY": api_key}
        )
    
    async def get_data(self, path: str, params: dict):
        async with self._session.get(url=path, params=params) as response:
            json = await response.json()

            return json['data']
    
    async def close_session(self):
        await self._session.connector.close()
        await self._session.close()