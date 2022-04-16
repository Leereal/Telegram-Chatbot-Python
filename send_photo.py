
import requests
from API import API

base_url = f"https://api.telegram.org/{API}/sendPhoto"

urls = [
    {"city": "https://unsplash.com/photos/xvJVDUoGpoU", "caption" : "City of Johhanesburg"},
    {"city": "https://unsplash.com/photos/CtqY0-G72qg", "caption" : "City of Harare"},
    {"city": "https://unsplash.com/photos/tUgJmmFwLPM", "caption" : "City of Pretoria"},
    {"city": "https://unsplash.com/photos/OjmO-dNF0lQ", "caption" : "City of Gaborone"},
    {"city": "https://unsplash.com/photos/g-krQzQo9mI", "caption" : "City of London"},
]

for city in urls :
    parameters = {
            "chat_id" : "-1001575169789",
            "photo" : city["city"],
            "caption" : city["caption"]
        }

    sendPhoto= requests.get(base_url,data=parameters)

    print(sendPhoto.text)