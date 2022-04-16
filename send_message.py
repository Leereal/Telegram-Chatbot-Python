
import requests
from API import API

base_url = f"https://api.telegram.org/{API}/sendMessage"

parameters = {
        "chat_id" : "-1001575169789",
        "text" : "This is a message"
    }

sendMessage = requests.get(base_url,data=parameters)

print(sendMessage.text)