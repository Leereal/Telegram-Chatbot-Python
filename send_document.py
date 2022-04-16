
import requests
from API import API

base_url = f"https://api.telegram.org/{API}/sendDocument"

parameters = {
        "chat_id" : "-1001575169789",    
        "caption" : "My Document"
    }

files = {"document": open("document/FXAuction.xlsx","rb")}


sendDoc= requests.get(base_url,data=parameters, files=files)

print(sendDoc.text)