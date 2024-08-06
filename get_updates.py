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




# Loop get updates
while True:
    # Get updates
    response = requests.get(URL)
    data = response.json()

    # Get results
    result = data['result']

    # Get last update
    last_update = result[-1]

    # Get last text from update
    text = get_text_from_update(last_update)

    # Print text
    print(text)