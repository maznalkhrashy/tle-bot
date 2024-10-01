import json
import os


print('R A D D E V : INSTALL MODULES ')

try: 
    import telebot 
except:
    os.system('python3 -m pip install telebot')
try: 
    import kvsqlite 
except:
    os.system('python3 -m pip install kvsqlite')

try: 
    import schedule 
except:
    os.system('python3 -m pip install schedule')

try: 
    import telebot 
except:
    os.system('python3 -m pip install requests')

try: 
    import user_agent 
except:
    os.system('python3 -m pip install user_agent')

try: 
    import base64 
except:
    os.system('python3 -m pip install base64')

try: 
    import ipaddress 
except:
    os.system('python3 -m pip install ipaddress')

try: 
    import struct 
except:
    os.system('python3 -m pip install struct')

try: 
    import pathlib 
except:
    os.system('python3 -m pip install pathlib')

try: 
    import typing 
except:
    os.system('python3 -m pip install typing')

try: 
    import aiosqlite 
except:
    os.system('python3 -m pip install aiosqlite')

try: 
    import telethon 
except:
    os.system('python3 -m pip install telethon')

try: 
    import pyrogram 
except:
    os.system('python3 -m pip install pyrogram')

try: 
    import opentele
except:
    os.system('python3 -m pip install opentele')

try: 
    import secrets 
except:
    os.system('python3 -m pip install secrets')

try: 
    import pyromod
except:
    os.system('python3 -m pip install pyromod')


def get_values_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    bot_token = data.get('bot_token')
    give_bot_token = data.get('give_bot_token')
    sudo = data.get('sudo')

    return bot_token, give_bot_token, sudo

def append_values_to_json(file_path, bot_token, give_bot_token, sudo):
    with open(file_path, 'r+', encoding='utf-8') as file:
        data = json.load(file)

        data['bot_token'] = bot_token
        data['give_bot_token'] = give_bot_token
        data['sudo'] = sudo

        file.seek(0)
        json.dump(data, file, indent=4, ensure_ascii=False)
        file.truncate()

# Example usage:
json_file_path = 'config.json'
bot_token = input('Add bot token: ')
give_bot_token = input('Add bot token of Give: ')
sudo = int(input('Add Sudo id: '))

# Get values from JSON
file_bot_token, file_give_bot_token, file_sudo = get_values_from_json(json_file_path)

# Update values
if bot_token:
    file_bot_token = bot_token
if give_bot_token:
    file_give_bot_token = give_bot_token
if sudo:
    file_sudo = sudo

append_values_to_json(json_file_path, file_bot_token, file_give_bot_token, file_sudo)
print("Ok")