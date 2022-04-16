
import requests
from API import API

base_url = f"https://api.telegram.org/{API}"

def read_message(offset):
    parameters = {
        "offset" : offset,
    }

    resp = requests.get(base_url + "/getUpdates",data=parameters)
    data = resp.json()

    print(data)

    for result in data["result"]:
        if "hi" in result["message"]["text"] :
            send_message()    
    
    if data["result"] :
        return data["result"][-1]["update_id"] + 1

def send_message():
    parameters = {
            "chat_id" : "-1001575169789",
            "text" : "Hello and how are you?"
        }
    resp = requests.get(base_url + "/sendMessage",data=parameters)
    print(resp.text)

offset = 0

while True:
    offset = read_message(offset)



