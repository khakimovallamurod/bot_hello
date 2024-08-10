import requests
import os
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'


def get_text_from_update(update):
    """
    Get text from update

    Args:
        update (dict): update

    Returns:
        str: text from update
    """
    return update['message']['text'] 

def get_chat_id_from_update(update):
    """
    Get chat id from update

    Args:
        update (dict): update

    Returns:
        int: chat id from update
    """
    return update['message']['chat']['id']




# Get updates
response = requests.get(URL)
print(response.json())
# Get text from update
print(get_text_from_update(response.json()['result'][0]))
# Get chat id from update
print(get_chat_id_from_update(response.json()['result'][0]))