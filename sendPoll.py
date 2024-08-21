import requests
import os
from pprint import pprint
TOKEN = os.environ['TOKEN'] 
import json

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
options = [
    {'text': '*Python*', 'text_parse_mode': "MarkdownV2"},
    {'text': '_C_', 'text_parse_mode': "MarkdownV2"},
    {'text': '__Packal__', 'text_parse_mode': "MarkdownV2"},
    {'text': "||JS||", 'text_parse_mode': "MarkdownV2"}
    ]

from pprint import pprint
pprint(send_poll(chat_id=1383186462, question='*Which* _programming_ __language__ ||is best?||', options=options))