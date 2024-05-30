import asyncio

from bot import launch_bot

if __name__ == '__main__':
    asyncio.run(launch_bot(_logging=False)) # level=logging.INFO