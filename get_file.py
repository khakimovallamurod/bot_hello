import requests
import os
from pprint import pprint
TOKEN = os.environ['TOKEN'] 

def get_file(file_id: str):
    """
    Get file

    Args:
        file_id (str): file id

    Returns:
        dict: file
    """
    URL = f'https://api.telegram.org/bot{TOKEN}/getFile'
    response = requests.get(URL, params={'file_id': file_id})
    return response.json()

def download_file(file_path: str):
    """
    Download file

    Args:
        file_path (str): file path

    Returns:
        bytes: file
    """
    URL = f'https://api.telegram.org/file/bot{TOKEN}/{file_path}'
    # Get file
    response = requests.get(URL)
    content = response.content
    # Save file
    with open(file_path, 'wb') as file:
        file.write(content)
    return True
    
    

file_id = 'AwACAgIAAxkBAAII72a27mYGItLQVnyTnL7J-a9WJy3fAAJSSwAC5D-4SU6Po_LmMx1sNQQ'


file_path = get_file(file_id)['result']['file_path']
print(file_path)
pprint(download_file(file_path))