import requests
import os
import time
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


def get_from_send_message(chat_id: int, text: str):
    btn1 = {'text': 'Apple'}
    btn1 = {'text': 'Apple'}
    response = requests.get(URL, params={'chat_id': chat_id, 'text': text})
        
    if response.status_code==200:
        return ('Send message accept')
    else:
        return ('Send message error')
chat_id = '1383186462'
text = 'Hello World!'

print(get_from_send_message(chat_id, text))

