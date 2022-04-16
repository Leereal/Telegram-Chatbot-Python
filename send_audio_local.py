
import requests

from API import API

base_url = f"https://api.telegram.org/{API}/sendAudio"



parameters = {
        "chat_id" : "-1001575169789",    
        "caption" : "Creative Minds"
    }

files = {"audio": open("audios/creativeminds.mp3","rb")}


sendAudio= requests.get(base_url,data=parameters, files=files)

print(sendAudio.text)