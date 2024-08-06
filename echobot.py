import requests
import os
import time
TOKEN = os.environ['TOKEN'] 

def get_url_reqests(endpoint: str):
    URL = f'https://api.telegram.org/bot{TOKEN}/'
    URL += endpoint
    return URL

def get_text_from_update(update):
    """
    Get text from update

    Args:
        update (dict): update

    Returns:
        str: text from update
    """
    return update['message']['chat']['id'], update['message']['text']

def get_from_send_message(chat_id: int, text: str):
    URL = get_url_reqests('sendMessage')
    response = requests.get(URL, params={'chat_id': chat_id, 'text': text})
        
    if response.status_code==200:
        return ('Send message accept')
    else:
        return ('Send message error')
    
last_id = -1
while True:
    response = requests.get(get_url_reqests('getUpdates'))
    data = response.json()
    result = data['result']
    
    update_last = result[-1]
    if last_id!=update_last['update_id']:
        chat_id, text = get_text_from_update(update_last)
        get_from_send_message(chat_id, text)


    last_id = update_last['update_id']
    time.sleep(0.5)