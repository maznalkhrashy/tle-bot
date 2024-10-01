from telethon import TelegramClient
import asyncio 


async def main():
    async with  TelegramClient('::mem', api_id=88, api_hash='dapp') as app:
        await app.start()




