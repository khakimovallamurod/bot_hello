import requests
import os
import time
TOKEN = os.environ['TOKEN'] 
def get_url_reqests(endpoint: str):
    URL = f'https://api.telegram.org/bot{TOKEN}/'
    URL += endpoint
    return URL
def send_message_keyboard(chat_id: int, text: str):
    btn1 = {'text': '👍', 'callback_data': 'like'}
    btn2 = {'text': '👎', 'callback_data': 'dislike'}
    btn3 = {'text': '🆑', 'callback_data': 'remove_like'}
    keyboard = [
        [btn1, btn2],
        [btn3]
    ]
    inline_keyboard = {
        'inline_keyboard': keyboard,
    }

    endpoint = 'sendMessage'
    URL = get_url_reqests(endpoint=endpoint)
    response = requests.post(URL, json={'chat_id': chat_id, 'text': text, 'reply_markup': inline_keyboard})
        
    if response.status_code==200:
        return ('Send message accept')
    else:
        return ('Send message error')


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
    url = get_url_reqests('sendMessage')
    response = requests.get(url, params={'chat_id': chat_id, 'text': text})
        
    if response.status_code==200:
        return ('Send message accept')
    else:
        return ('Send message error')

like_or_dislike = {
    'like': 0,
    'dislike': 0
}

last_id = -1
while True:
    url = get_url_reqests(endpoint='getUpdates')
    response = requests.get(url)
    data = response.json()
    result = data['result']
    
    update_last = result[-1]
    if last_id!=update_last['update_id']:
        update_end = get_text_from_update(update_last)
        if update_end.get('text')!=None :
            send_message_keyboard(chat_id=update_end['chat']['id'], text="Like or Dislike")
            if update_end['text']=='👍':
                like_or_dislike['like'] += 1
            if update_end['text'] == '👎':
                like_or_dislike['dislike'] += 1
            if update_end['text']=='🆑':
                like_or_dislike['like'] = 0
                like_or_dislike['dislike'] = 0
            get_from_send_message(chat_id=update_end['chat']['id'], text=f"Like count: {like_or_dislike['like']}\nDislike count: {like_or_dislike['dislike']}")
    last_id = update_last['update_id']
    time.sleep(0.5)

# Get updates  


