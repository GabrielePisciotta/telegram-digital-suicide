# Telegram Digital Suicide
The purpose of this script is to compensate for the lack of an official feature in Telegram to delete **all** the messages you've
sent in specified groups, committing a so called «digital suicide».

## Install dependency
```$ pip3 install Telethon```

## Modify config.py
There are four parameters you have to set:
- api_id 
- api_hash 
- my_id 
- groups

The first two you'll have to take following [this guide](https://core.telegram.org/api/obtaining_api_id).
The 3rd is your personal ID associated to your username, and you can take it using [this bot](https://t.me/userinfobot).
The 4th is the one that let you specify all the groups in which you want to delete your messages. You have to specify
for each one a tuple `(group_username, last_message_id)`. You can get the last message's id by simply getting the link
of the last message.


## Run
```$ python3 suicide.py```

