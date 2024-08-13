import requests
import os
import time
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
# r = requests.get(f'https://api.telegram.org/bot{TOKEN}/deleteWebhook')

def get_text_from_update(update):
    """
    Get text from update

    Args:
        update (dict): update

    Returns:
        str: text from update
    """
    return update['message']['text']

<<<<<<< HEAD
last_id = -1
while True:
    response = requests.get(URL)
    data = response.json()
    result = data['result']
    
    update_last = result[-1]
    if last_id!=update_last['update_id']:
        update_end = get_text_from_update(update_last)
        print(update_end)
    last_id = update_last['update_id']
    time.sleep(0.5)
    
# Get updates  

=======
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
>>>>>>> b86b87f7b661fd43db0664a2929e9c67f447821c
