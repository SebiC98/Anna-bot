import os
import requests
import time

API_KEY = os.environ['annaApi']



def welcome_msg(item):
  chat_id = item["message"]["chat"]["id"]
  user_id = item["message"]["new_chat_member"]["id"]
  user_name = item["message"]["new_chat_member"].get("username", user_id)

  welcome_msg = ''' <a href="tg://user?id={}">@{}</a>, bine ai venit pe grupul Forza Horizon 5 Romania 🇷🇴! '''.format(user_id, user_name)

  to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(API_KEY, chat_id, welcome_msg)
  resp = requests.get(to_url)

import datetime

endTime = datetime.datetime.now() + datetime.timedelta(minutes=3)

base_url = 'https://api.telegram.org/bot{}/getUpdates'.format(API_KEY)
resp = requests.get(base_url)
data = resp.json()
for item in data["result"]:
  old_id = item["update_id"]

while endTime > datetime.datetime.now():
  time.sleep(1)
  base_url = 'https://api.telegram.org/bot{}/getUpdates'.format(API_KEY)
  resp = requests.get(base_url)
  data = resp.json()

  for item in data["result"]:
    new_id = item["update_id"]
    if old_id < new_id:
      old_id = item["update_id"]
      try:
        if "new_chat_member" in item["message"]:
          welcome_msg(item)
          print(new_id)
      except:
        pass

