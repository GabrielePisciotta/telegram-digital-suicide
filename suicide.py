from telethon import TelegramClient
from config import *

# You'll be asked to insert your mobile phone number and the OTP
client = TelegramClient('session', api_id, api_hash).start()

deleted_count = 0
for group_username, max in groups:
    print("[+] Suiciding from group: {}".format(group_username))

    messages = []
    chats = client.get_messages(group_username,
                                max_id=max,
                                min_id=0,
                                reverse=True)

    if len(chats):

        for chat in chats:
                if chat.from_id == my_id:
                        client.delete_messages(group_username, [chat.id])
                        deleted_count += 1


print("[+] (OK) Suicide finished! Deleted {} messages".format(deleted_count))

