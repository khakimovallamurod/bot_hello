import requests
import os
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/getMe'

# Get bot information
import asyncio
import aiohttp


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('https://randomuser.me/api') as response:


            
            import time
            data = await response.json()

            return data['results'][0]['name']['first']
            
print('Started')
name=asyncio.run(main())
print(name)
print('Finished')

