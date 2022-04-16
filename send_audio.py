
import requests
from API import API

base_url = f"https://api.telegram.org/{API}/sendAudio"

urls = [
    {"audio": "https://www.bensound.com/bensound-music/bensound-creativeminds.mp3", "caption" : "Creative Minds"},
]

for audio in urls :
    parameters = {
            "chat_id" : "-1001575169789",
            "audio" : audio["audio"],
            "caption" : audio["caption"]
        }

    sendAudio= requests.get(base_url,data=parameters)

    print(sendAudio.text)