import pandas as pd
import requests
from API import API


base_url = f"https://api.telegram.org/{API}"


file = "document/qna.tsv"

df = pd.read_csv(file, sep="\t")

def read_message(offset):
    parameters = {
        "offset" : offset,
    }

    resp = requests.get(base_url + "/getUpdates",data=parameters)
    data = resp.json()

    print(data)

    for result in data["result"]:
        try:
            send_message(result) 
        except KeyError:
            send_message("No message")   
        else:
            pass 
    
    if data["result"] :
        return data["result"][-1]["update_id"] + 1

def auto_answer(message):
    if message == "Edited Message":
        return " Sorry, I don't respond to edited messages"
    else:
        answer = df.loc[df["Question"].str.lower() == message.lower()]

        if not answer.empty:
            answer = answer.iloc[0]['Answer']
            return answer
        else:
            return " Sorry, I could not understand you !!! I am still learning and try to get better in answering."
        

def send_message(message):
    message_id = 0

    try:        
        text = message["message"]["text"]
    except TypeError:
        answer = auto_answer("Edited Message")
    else:
        answer = auto_answer(text)
        message_id = message["message"]["message_id"]       
        
      
    parameters = {
            "chat_id" : "-1001575169789",
            "text" : answer,
            "reply_to_message_id" : message_id
        }

    resp = requests.get(base_url + "/sendMessage",data=parameters)
    print(resp.text)

offset = 0

while True:
    offset = read_message(offset)



