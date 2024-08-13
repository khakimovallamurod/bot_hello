import requests
import os
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/getUserProfilePhotos'


def getUserProfilePhotos(chat_id: int):
    response = requests.get(URL, params={'chat_id': chat_id})
    print(response.status_code)
    return (response.json())
    
chat_id = 5907682059
print(getUserProfilePhotos(chat_id))
