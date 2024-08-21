import requests
import os
import time
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
