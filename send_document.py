import requests
import os
<<<<<<< HEAD
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
=======
from pprint import pprint
TOKEN = os.environ['TOKEN'] 

def send_document(chat_id: int, document: str):
    """
    Send document

    Args:
        chat_id (int): chat id
        document (str): document
    """
    URL = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
    response = requests.post(URL, params={'chat_id': chat_id}, files={'document': document})
    return response.json()


chat_id = 86775091
FILE_PATH = 'README.md'

document = open(FILE_PATH, 'rb').read()
pprint(send_document(chat_id, document))
>>>>>>> b86b87f7b661fd43db0664a2929e9c67f447821c
