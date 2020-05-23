import os, sys
from time import sleep
from telethon import TelegramClient, sync, events
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
if not os.path.exists("session"):
   os.makedirs("session")

api_id = 1359062
api_hash = 'e373e9ed12f9264e5c3fd957a153859f'

phone = sys.argv[1]

client = TelegramClient("session/"+phone,api_id,api_hash)
client.connect()


if not client.is_user_authorized():
   try:
     client.send_code_request(phone)
     client.sign_in(phone,input("Nhập Code : "))
   except SessionPasswordNeededError:
     client.start(phone,input("Enter code 2fa : "))
client.get_me()
bot = client.get_entity("@fastdogeclaimbot")

print("\033[1;31mCreator : \033[1;32mVQH Tổng Hợp")
while(True):
   client.send_message(entity=bot,message="🎁 Claim Bonus")
   print("\033[1;31mBạn nhận được: \033[1;31m1.5 DOGE")
   sleep(21610)

