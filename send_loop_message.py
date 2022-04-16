import time
import requests
from API import API

base_url = f"https://api.telegram.org/{API}/sendMessage"

jokes = ["Joke 1","Joke 2","Joke 3","Joke 4"]
for joke in jokes:
    time.sleep(10)
    parameters = {
            "chat_id" : "-1001575169789",
            "text" : joke
        }

    sendMessage = requests.get(base_url,data=parameters)

    print(sendMessage.text)