import requests
import os
import time
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/sendDocument'


def send_document(chat_id: int, file_path: str):
    # response = requests.get(URL, params={'chat_id': chat_id, 'document': file_path})
    response = requests.post(URL, params={'chat_id': chat_id}, files={'document': file_path})
        
    if response.status_code==200:
        return ('Send document accept')
    else:
        return ('Send document error')
chat_id = '1383186462'
file = open('dataset.csv', 'rb').read()
 
print(send_document(chat_id, file))
