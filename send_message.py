import requests
import os
<<<<<<< HEAD
import time
=======
>>>>>>> b86b87f7b661fd43db0664a2929e9c67f447821c
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


<<<<<<< HEAD
def get_from_send_message(chat_id: int, text: str):
    response = requests.get(URL, params={'chat_id': chat_id, 'text': text})
        
    if response.status_code==200:
        return ('Send message accept')
    else:
        return ('Send message error')
chat_id = '1383186462'
text = 'Hello World!'

print(get_from_send_message(chat_id, text))
=======


def send_message(chat_id: int, text: str):
    """
    Send message

    Args:
        chat_id (int): chat id
        text (str): text
    """
    response = requests.get(URL, params={'chat_id': chat_id, 'text': text})
    return response.json()

chat_id = 86775091
text = 'Hello, World!'

send_message(chat_id, text)
>>>>>>> b86b87f7b661fd43db0664a2929e9c67f447821c
