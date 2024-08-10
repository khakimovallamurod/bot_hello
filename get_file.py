
import requests
import os
from pprint import pprint

from openai import OpenAI

# Get Open AI API key
TOKEN_OPENAI = os.environ['TOKEN_OPENAI']
# Get Telegram API key
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

    
    return content

def speech_to_text(file_content: bytes):
    """
    Speech to text

    Args:
        file_content (bytes): file content

    Returns:
        str: text
    """
    client = OpenAI(api_key=TOKEN_OPENAI,base_url="https://api.lemonfox.ai/v1")
    transcription = client.audio.transcriptions.create(

        model='whisper-1',
        file=file_content
    ) 

    return transcription

    
    

file_id = ''


file_path = get_file(file_id)['result']['file_path']
print(file_path)

file_content = download_file(file_path)
text = speech_to_text(file_content)
print(text)



