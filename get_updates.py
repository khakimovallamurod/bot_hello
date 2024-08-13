import requests
import os
import time
import get_file

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
    return update['message']


def get_chat_id_from_update(update):
    """
    Get chat id from update

    Args:
        update (dict): update

    Returns:
        int: chat id from update
    """
    return update['message']['chat']['id']

def get_from_send_message(chat_id: int, text: str):
    response = requests.get(URL, params={'chat_id': chat_id, 'text': text})
        
    if response.status_code==200:
        return ('Send message accept')
    else:
        return ('Send message error')


last_id = -1
while True:
    response = requests.get(URL)
    data = response.json()
    result = data['result']
    
    update_last = result[-1]
    if last_id!=update_last['update_id']:
        update_end = get_text_from_update(update_last)
        if update_end.get('text')!=None:
            get_from_send_message(chat_id=update_end['chat']['id'], text=update_end['text'])
        elif update_end.get('voice')!=None:
            file_id = update_end['voice']['file_id']
            file_path = get_file.get_file(file_id)['result']['file_path']
            print(file_path)

            file_content = get_file.download_file(file_path)
            text = get_file.speech_to_text(file_content)
            print(file_content)
            get_from_send_message(chat_id=update_end['chat']['id'], text=text)

    last_id = update_last['update_id']
    time.sleep(0.5)

# Get updates  




# Get updates
response = requests.get(URL)
print(response.json())
# Get text from update
print(get_text_from_update(response.json()['result'][0]))
# Get chat id from update
print(get_chat_id_from_update(response.json()['result'][0]))
