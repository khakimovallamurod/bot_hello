import requests
import os
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
