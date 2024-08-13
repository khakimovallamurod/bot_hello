import requests
import os
<<<<<<< HEAD
import time
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'


def send_photoes(chat_id: int, file_path: str):
    response = requests.get(URL, params={'chat_id': chat_id, 'photo': file_path})
        
    if response.status_code==200:
        return ('Send photo accept')
    else:
        return ('Send photo error')
chat_id = '1383186462'
file_path = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbqxbo4AfaWlCoT_8mfRirS5DxB91ha244oA&s'

print(send_photoes(chat_id, file_path))
=======
from pprint import pprint
TOKEN = os.environ['TOKEN'] 


def send_photo(chat_id: int, photo: str):
    """
    Send photo

    Args:
        chat_id (int): chat id
        photo (str): photo
    """
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    response = requests.get(URL, params={'chat_id': chat_id, 'photo': photo})
    return response.json()


chat_id = 86775091
url = 'AgACAgQAAxkDAAII22a0X_ncnUvEyA5FyO46in4qXM5FAALltDEb0Wx9UY8z0lzlrnBqAQADAgADcwADNQQ'

pprint(send_photo(chat_id, url))
>>>>>>> b86b87f7b661fd43db0664a2929e9c67f447821c
