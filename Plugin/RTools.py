import json 
from threading import Timer
import requests 
from telebot import TeleBot
import random


class dataS:
    def __init__(self):
        self.PAT = r'datas/cods.json'

    def GET_DATA(self):
        with open(self.PAT, 'r') as JSObj:
            data = json.load(JSObj)
        return data
    
    def UPDATE_DATA(self, NEW_DATA):
        with open(self.PAT, 'w') as JSObj:
            json.dump(NEW_DATA,JSObj,indent=3)

    def GET_CODE(self, code: str):
        data = self.GET_DATA()
        return data[code]
    
    def CODE_EXISTS(self, code: str):
        data = self.GET_DATA()
        return code in data['code']

    def NEW_CODE(self,code: str, coin: int, mem: int):
        data = self.GET_DATA()
        data['code'].update({code:{'coin':coin, 'mem':mem,'users':[]}})
        self.UPDATE_DATA(data)
        
    def NEW_USER_CODE(self,code: str, coin: int,user_id: int):
        data = self.GET_DATA()
        data['code'].update({code:{'coin':coin, 'mem':1,'user_id':user_id,'users':[]}})
        self.UPDATE_DATA(data)



class ApiTelegram:

    def __init__(self, API_KEY: str):
        self.API_KEY = API_KEY
        self.API_URL = f"https://api.telegram.org/bot{self.API_KEY}/"

    def SEND_DOCUMENT(self,chat_id, file_path: str,caption: str = None):
        with open(file_path, 'rb') as backup:
            requests.post(self.API_URL + "sendDocument", data={'chat_id': chat_id,'caption':caption}, files={'document': backup})
        
    


def DELET_MESSAGE_AD(bot: TeleBot, message_id, chat_id):
    bot.delete_message(chat_id, message_id)

def START_DELET_TIMER_AD(hours: int, bot,  message_id, chat_id):
    seconds = hours * 3600
    Time = Timer(seconds, DELET_MESSAGE_AD, args=(bot, message_id, chat_id,)).start()


def RAND_CODE():
    CODE = ''
    for i in range(20):
        CODE=CODE+random.choice('abcdefjhijklmnopqrstuvwxyz' + '1234567890')
    return CODE

