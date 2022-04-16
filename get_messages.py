
import requests

API = "https://api.telegram.org/bot5243368882:AAFQAXYnAMosieDwRYB5DFrkju-4DadwdZM/getUpdates"

parameters = {
    "offset" : "462081755",
    "limit" : "3"
}

messages = requests.get(API,data=parameters)
print(messages.text)

