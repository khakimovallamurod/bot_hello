import requests
import os
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
    response = requests.get(URL)
    data = response.json()['result']
    update_id = update['update_id']
    for update_item in data:
        if update_item['update_id'] == update_id:
            return update_item['text']
    return 'Update not found'
# Get updates

