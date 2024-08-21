import requests
import os

url = "https://api.lemonfox.ai/v1/audio/transcriptions"
TOKEN_OPENAI = os.environ['TOKEN_OPENAI']
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
    headers = {
      "Authorization": TOKEN_OPENAI
    }
    
    data = {
      "file": file_content,
      "language": "english",
      "response_format": "json"
    }
    files = {'file': file_content}
    response = requests.post(url, headers=headers, files=files, data=data)
    
    return response.json()

file_id = 'AwACAgIAAxkBAANGZrsgXSoKBwvePX1sWA16JKZQ4CIAAv9WAAL5C9hJnJpeeOq-Lao1BA'
file_path = get_file(file_id)['result']['file_path']
file_content = download_file(file_path)
# response = requests.post(url, headers=headers, data=data)
# print(response.json())
print(speech_to_text(file_content))

