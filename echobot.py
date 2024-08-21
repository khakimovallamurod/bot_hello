import requests
import os
import time
from speach_to_text import get_file, download_file, speech_to_text
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
    return update['message']['chat']['id'], update['message']

def get_from_send_message(chat_id: int, text: str):
    URL = get_url_reqests('sendMessage')
    response = requests.get(URL, params={'chat_id': chat_id, 'text': text})
        
    if response.status_code==200:
        return ('Send message accept')
    else:
        return ('Send message error')

def send_poll(chat_id: int, question: str, options: list):
    """
    Send poll

    Args:
        chat_id (int): chat id
        question (str): question
        options (list): options
    """
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPoll'
    response = requests.post(URL, json={
        'chat_id': chat_id, 
        'question': question, 
        'options': options,
        'question_parse_mode': "MarkdownV2",
        'type': 'quiz',
        'is_anonymous': False,
        'allows_multiple_answers': False,
        "correct_option_id": 0
        })

    return response.json()

last_id = -1
while True:
    response = requests.get(get_url_reqests('getUpdates'))
    data = response.json()
    result = data['result']
    
    update_last = result[-1]
    if last_id!=update_last['update_id']:
        chat_id, update_end = get_text_from_update(update_last)
        if update_end.get('poll')!=None:
            options = update_end['poll']['options']
            question = update_end['poll']['question']
            send_poll(chat_id=chat_id, options=options, question=question)
        
        elif update_end.get('text')!=None:
            get_from_send_message(chat_id, update_end['text'])
        elif update_end.get('voice')!=None:
            file_id = update_end['voice']['file_id']
            file_path = get_file(file_id)['result']['file_path']
            # print(file_path)
            file_content = download_file(file_path)
            speach_text = speech_to_text(file_content)
            get_from_send_message(chat_id, speach_text.get('text'))
            # print(file_content)
            print(speach_text)


    last_id = update_last['update_id']
    time.sleep(0.5)