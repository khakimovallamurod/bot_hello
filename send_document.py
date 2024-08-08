import requests
import os
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