import os,requests
from Plugin.RadPLugin import MangSession
from Plugin.dbs import *
from Plugin.apis import *
from Plugin.dbs import Givt,statck
from Plugin.tempdata import USER_TEMP
from Plugin.functions import *
from Plugin.RTools import dataS, START_DELET_TIMER_AD, RAND_CODE
from Plugin.edit_price import *
import shutil
import zipfile
AD_CHANNL = '@mw_dc'
AD_REQUEST_CHANNL = '@MoooomOam102'

REACTIONS_LIST = {
    '1':['🥰', '🔥', '👍', '❤️','🎉'],
    '2':['🤮','💩','👎','🖕'],
    '3':['❤️‍🔥','🤯', '🍌', '⚡️'],
}


datas = dataS()
Db = data()
if not os.path.isdir('dbs'):
    os.mkdir('dbs')
try:
    import telebot, json, os, time, re, threading, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio

    import time
    import requests
    from user_agent import generate_user_agent
    import datetime
    import base64
    import ipaddress
    import struct
    from pathlib import Path
    from typing import Type
    import shutil
    import zipfile
    import aiosqlite
    from opentele.api import APIData
    from pyrogram.session.internals.data_center import DataCenter
    from telethon import TelegramClient
    from telethon.sessions import StringSession
    import secrets
    from opentele.api import API, APIData
    from pyrogram.client import Client

except:
    os.system('python3 -m pip install telebot pyrogram tgcrypto kvsqlite pyromod==1.4 schedule')
    import telebot, json, os, time, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk


ad_temp = {}

w = json.loads(open('config.json', 'r+',encoding="utf8").read())
token = w['bot_token']
stypes = ['member', 'administrator', 'creator']

PRICES = json.load(open("./datas/prices.json"))

ad_price = 1000
stk = statck()

view_stories_price = db.get("view_stories_price") if db.exists("view_stories_price") else 1
rect_stories_price = db.get("view_stories_price") if db.exists("view_stories_price") else 1
member_price = db.get("member_price") if db.exists("member_price") else 20
vote_price = db.get("vote_price") if db.exists("vote_price") else 20
spam_price = db.get("spam_price") if db.exists("spam_price") else 10
react_price = db.get("react_price") if db.exists("react_price") else 2
forward_price = db.get("forward_price") if db.exists("forward_price") else 2
view_price = db.get("view_price") if db.exists("view_price") else 1
poll_price = db.get("poll_price") if db.exists("poll_price") else 2
comment_price = db.get("comment_price") if db.exists("comment_price") else 12
link_price = db.get("link_price") if db.exists("link_price") else 200
linkbot2_price = db.get("link_price") if db.exists("link_price") else 20
userbot_price = db.get("userbot_price") if db.exists("userbot_price") else 20
linkbot_price = db.get("linkbot2_price") if db.exists("linkbot2_price") else 20
story_price = db.get("story_price") if db.exists("story_price") else 20

db = uu('dbs/service.trakos', 'trakos_bot')

bk = mk(row_width=1).add(btn('‹ رجوع ↻›', callback_data='back'))
db.set('force', [])
token_bot = "6521386128:AAHzYG687XIAtSxeLoygqm3Tr8TxRqxHiX0" # توكن البوت الاساس
token_helper = "6529701235:AAFVgfzQJklNH49pQ8P0fSyxdHBb4ZfpnUs" #توكن بوت المساعد

bot = TeleBot(token=token_bot,num_threads=45,threaded=True,skip_pending=True,parse_mode='html', disable_web_page_preview=True)

bot2 = TeleBot(token=token_helper,num_threads=45,threaded=True,skip_pending=True,parse_mode='Markdown', disable_web_page_preview=True)


if not db.get('accounts'):
    db.set('accounts', [])
    pass
if not db.get('accounts_t'):
    db.set('accounts_t', [])
if not db.get('chat_blacklist'):
    db.set('chat_blacklist', [])
sudos = 6360165330 #الادمن
if not db.get("admins"):
    db.set('admins', [sudos,6360165330, 6700475002, ])
if not db.get('badguys'):
    db.set('badguys', [])
if not db.get('force'):
    db.set('force', [])
sudo = w['sudo']
def force(channel, userid):
    try:
        x = bot.get_chat_member(channel, userid)
        ##print(x)
    except:
        return True
    if str(x.status) in stypes:
        ##print(x)
        return True
    else:
        ##print(x)
        return False
def addord():
    if not db.get('orders'):
        db.set('orders', 1)
        return True
    else:
        d = db.get('orders')
        d+=1
        db.set('orders', d)
        return True
def check_vip(user_id):
    users = db.get(f"vip_{user_id}")
    noww = time.time()
    if db.exists(f"vip_{user_id}"):
        last_time = users['vip']
        timeee = int(db.get(f"vipp_{user_id}_time"))
        WAIT_TIMEE = int(timeee) * 24 * 60 * 60
        elapsed_time = noww - last_time
        if elapsed_time < WAIT_TIMEE:
            remaining_time = WAIT_TIMEE - elapsed_time
            return int(remaining_time)
        else:
            return None
    else:
        return None
bbs = token_bot
bbb = token_helper

def CeckAnjoens(id):
    REs =Db.Get(id)
    
    for chatID in REs:
        ##print(chatID)
        Status = requests.get(f"https://api.telegram.org/bot{token_helper}/getChatMember?chat_id={chatID}&user_id={id}").json()
        ##print(Status)
        if Status["result"]["status"] == "left":
            ##print("0000000000000000000000000000000000000")
            bot.send_message(chat_id=int(id), text=f"• تم خصم منك 20 نقطة لأنك غادرت من قناة {chatID} .")
            b = db.get(f'user_{id}')
            b['coins']-=20
            db.set(f'user_{id}', b)
            Db.de(id)
            
            
        

# CeckAnjoens(6134717243)
# exit()
@bot.message_handler(regexp='^/start$')
def start_message(message):
    if message.from_user.id == 6360165330:
        bot.send_message(message.chat.id, 'God By ..')
    try:
        bot.delete_message(message.chat.id, USER_TEMP[message.from_user.id]['call']['id'])
    except:
        pass
    user_id = message.from_user.id
    if not user_id in USER_TEMP:
        USER_TEMP.update({user_id:{'trans':{'id':None},'call':{'id':None}, 'code':{'id':None}}})
    btn059 = btn('.', callback_data='zip_all')
    count_ord = db.get('orders') if db.get('orders') else 1
    a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
    for temp in a:
        db.delete(f'{a}_{user_id}_proccess')
    keys = mk(row_width=2)
    if user_id in db.get("admins") or user_id == sudo:
        keys_ = mk()
        btn01 = btn('الاحصائيات', callback_data='stats')
        btn02 = btn("اذاعة", callback_data='cast')
        btn05, btn06 = btn('حظر شخص', callback_data='banone'), btn('فك حظر', callback_data='unbanone')
        btn09 = btn('معرفة عدد الارقام', callback_data='numbers')
        btna = btn('تفعيل ᵛ͢ᵎᵖ', callback_data='addvip')
        btnl = btn('الغاء ᵛ͢ᵎᵖ', callback_data='lesvip')
        leave = btn('مغادرة كل الحسابات من قناة', callback_data='leave')
        lvall = btn('مغادرة كل القنوات  والمجموعات وحظر البوتات', callback_data='lvall')
        keys_.add(btn01, btn02)
        keys_.add(btn05, btn06)
        keys_.add(leave)
        btn11 = btn('تعيين قنوات الاشتراك', callback_data='setforce')
        btn10 = btn('اضافه نقاط ', callback_data='addpoints')
        les = btn('خصم نقاط', callback_data='lespoints')
        btn03 = btn('اضافة ادمن', callback_data='addadmin')
        btn04 = btn('مسح ادمن', callback_data='deladmin')
        btn012 = btn('الادمنية ', callback_data='admins')
        btn013 = btn('سحب الاصوات', callback_data='dump_votes')
        btn014 = btn('جلب معلومات شخص', callback_data='get_info')
        btn015 = btn("تنظيف الحسابات", callback_data='clear')
        btn016= btn("تحويل الحسابات Telethon", callback_data='pyr_to_teleh')
        btn017 = btn('تعيين نقاط الدخول', callback_data='entre_bot')
        ch = btn('تغيير سعر خدمة  ', callback_data='change_price')
        ch2 = btn('تغيير سعر خدمة ᵛ͢ᵎᵖ', callback_data='change_price_vip')
        crcode = btn('انشاء كود هدية', callback_data='create_code_coin')
        btn059 = btn('.', callback_data='zip_all')
        keys_.add(btn03, btn04)
        keys_.add(btn10, les)
        keys_.add(btn012, btn11)
        keys_.add(lvall)   
        keys_.add(btn09)
        keys_.add(btna, btnl)
        keys_.add(btn014, btn013)
        keys_.add(btn015, btn016)
        keys_.add(btn017)
        keys_.add(ch, ch2)
        keys_.add(crcode)
        bot.reply_to(message, '**• اهلا بك في لوحه الأدمن الخاصه بالبوت 🤖**\n\n- يمكنك التحكم في البوت الخاص بك من هنا \n\n===================', reply_markup=keys_)
    if user_id in db.get('badguys'): return
    if not db.get(f'user_{user_id}'):
        do = db.get('force')
        if do != None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                if str(x.status) in stypes:
                    pass
                else:
                    bot.reply_to(message, f'• عليك الاشترك بقناة البوت اولا \n • @{channel}')
                    return
        xx = int(db.get("entre_bot")) if db.exists("entre_bot") else 0
        data = {'id': user_id, 'users': [], 'coins': xx, 'premium': False}
        set_user(user_id, data)
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        bot.send_message(chat_id=int(sudo), text=f'٭ *تم دخول شخص جديد الى البوت الخاص بك 👾*\n\n•_ معلومات العضو الجديد ._\n\n• الاسم : {message.from_user.first_name}\n• المعرف : @{message.from_user.username}\n• الايدي : {message.from_user.id}\n\n*• عدد الاعضاء الكلي* : {good}', parse_mode="Markdown")
        coin = get(user_id)['coins']
        # ex : radfx2 

        ############
        btn0 = btn(f'نقاطك : {coin} IQD', callback_data='none')
        btn1 = btn(f'‹قسم خدمات الرشق›', callback_data='service')
        btn03 = btn('‹اعدادات حسابك ›️', callback_data='settings')
        btn4 = btn('‹تجميع رصيد›', callback_data='collect')
        btn5 = btn('‹تحويل رصيد›', callback_data='send')
        btn01 = btn(f'‹استخدام كود›', callback_data='codecoin')
        btn60 = btn(' مطور البوت ', url='https://t.me/i_n_ub')
        btn7 = btn('‹شراء رصيد›', callback_data='buy')
        btn100 = btn('‹شريط المهام›', callback_data='tape')
        if message.from_user.first_name == ".":
            keys.add(btn059)
        keys.add(btn0)
        keys.add(btn1)
        keys.add(btn4, btn7)
        keys.add(btn5, btn03)
        keys.add(btn01)
        keys.add(btn60)
        keys.add(btn100)
        keys.add(btn(f'عدد الطلبات : {count_ord} ', callback_data=' 4560'))
        mm = f"""-  بوت خدمات_ 𝐌𝐙 متميز بسرعة✓ .
- رشق, تصويت, تفاعلات, مشاهدات
- سبام,كروبات, سبام, رسائل, خاص ✓ . """
        
        ssid = bot.reply_to(message, mm, reply_markup=keys)
        USER_TEMP[message.from_user.id]['call']['id'] = ssid.id
        return ssid
    do = db.get('force')
    if do is not None:
        for channel in do:
            x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
            if str(x.status) in stypes:
                pass
            else:
                bot.reply_to(message, f'🚸| لطفاً أخي:🖤.🔰| عليك الأشتراك بقناة البوت لتتمكن \nمن أستخدام : 💻 \n- @{channel}\n\n‼️| أشترك ثم أرسل /start ')
                return
    if str(message.from_user.first_name) == ".":
        keys.add(btn059)
    coin = get(user_id)['coins']
    btn0 = btn(f'نقاطك : {coin} IQD', callback_data='none')
    btn1 = btn(f'‹قسم خدمات الرشق›', callback_data='service')
    btn4 = btn('‹تجميع رصيد›', callback_data='collect')
    btn5 = btn('‹تحويل رصيد›', callback_data='send')
    btn01 = btn(f'‹استخدام كود›', callback_data='codecoin')
    btn60 = btn('‹قناة البوت›', url='https://t.me/mw_dc')
    btn7 = btn('‹شراء رصيد›', callback_data='buy')
    btn03 = btn('‹اعدادات حسابك›️', callback_data='settings')
    btn100 = btn('‹شريط المهام›', callback_data='tape')
    keys.add(btn0)
    keys.add(btn1)
    keys.add(btn4, btn7)
    keys.add(btn5, btn03)
    keys.add(btn01)
    keys.add(btn60)
    keys.add(btn100)
    keys.add(btn(f'عدد الطلبات : {count_ord} ', callback_data=' 4560'))
    mm = f"""⌁︙مرحبا بك في بوت خدمات_ 𝐌𝐙 ✨
⌁︙حسابات البوت جميعها عربية حقيقية ✨
⌁︙البوت يمتاز بسرعة تنفيذ الطلب ✨ """
    # return bot.reply_to(message, mm, reply_markup=keys)
    ssid = bot.reply_to(message, mm, reply_markup=keys)
    USER_TEMP[message.from_user.id]['call']['id'] = ssid.id
    return ssid


@bot.message_handler(regexp='^/start (.*)')
def start_asinvite(message):
    join_user = message.from_user.id

    to_user = int(message.text.split("/start ")[1])
    if join_user == to_user:
        start_message(message)
        bot.send_message(join_user,f'لا يمكنك الدخول عبر الرابط الخاص بك ❌')
        return
    if not check_user(join_user):
        someinfo = get(to_user)
        if join_user in someinfo['users']:
            start_message(message)
            return
        else:
            dd = link_price
            someinfo['users'].append(join_user)
            someinfo['coins'] = int(someinfo['coins']) + dd
            xx = int(db.get("entre_bot")) if db.exists("entre_bot") else 0
            info = {'coins': xx, 'id': join_user, 'premium': False, "users": []}
            set_user(join_user, info)
            set_user(to_user, someinfo)
            bot.send_message(to_user,f'• قام <code>{message.from_user.id}</code> بالدخول الى رابط الدعوة الخاص بك وحصلت علي {dd} نقطة 🎉')
        typ = float(db.get(f"typ_{to_user}")) if db.exists(f"typ_{to_user}") else 0.0
        ftt = typ + 0.3
        db.set(f"typ_{to_user}", float(ftt))
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        bot.send_message(chat_id=int(sudo), text=f'٭ *تم دخول شخص جديد الى البوت الخاص بك 👾*\n\n•_ معلومات العضو الجديد ._\n\n• الاسم : {message.from_user.first_name}\n• المعرف : @{message.from_user.username}\n• الايدي : {message.from_user.id}\n\n*• عدد الاعضاء الكلي* : {good}', parse_mode="Markdown")
def giiiift(user_id):
    users = db.get(f"us_{user_id}_giftt")
    noww = time.time()
    WAIT_TIMEE = 24 * 60 * 60
    if db.exists(f"us_{user_id}_giftt"):
        last_time = users['timee']
        elapsed_time = noww - last_time
        if elapsed_time < WAIT_TIMEE:
            remaining_time = WAIT_TIMEE - elapsed_time
            return int(remaining_time)
        else:
            return None
    else:
        return None
        start_message(message)
        return

@bot.callback_query_handler(func=lambda c: True)
def c_rs(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    do = db.get('force')
    count_ord = db.get('orders') if db.get('orders') else 1
    if do != None:
        for channel in do:
            x = bot.get_chat_member(chat_id="@"+channel, user_id=cid)
            if str(x.status) in stypes:
                pass
            else:
                bot.edit_message_text(text=f'🚸| لطفاً أخي:🖤.🔰| عليك الأشتراك بقناة البوت لتتمكن \nمن أستخدام : 💻 \n- @{channel}\n\n‼️| أشترك ثم أرسل /start ', chat_id=cid, message_id=mid)
                return
    admins = db.get('admins')
    d = db.get('admins')
    a = ['leave', 'member', 'vote', 'spam']
    for temp in a:
        db.delete(f'{a}_{cid}_proccess')
    if data == 'stats':
        good = 0
        users = db.keys('user_%')
        
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
                ##print(d)
            except: continue
        bot.edit_message_text(text=f'• عدد اعضاء البوت : {good}', chat_id=cid, message_id=mid)
        return
    if data == 'entre_bot':
        x = bot.edit_message_text(text='⌁︙ارسل عدد نقاط الدخول الان', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, entre_bot)
    if data == '_givt':
        keys = mk(
            [
                
                [btn(text='‹ رجوع ↻›', callback_data='sttat')]
            ]
        )
        bot.edit_message_text(text="""⌁︙مرحبا بك في قسم جوائز مشاركات رابط الدعوة
المستوى الأول ~ يحصل على 1000 IQD لكل 10 مشاركات و اشتراك ᵛ͢ᵎᵖ لمدة أسبوعين لكل 500 مشاركة
المستوى الثاني ~ يحصل على 15000 IQD لكل 100 مشاركة و ᵛ͢ᵎᵖ لمدة أسبوعين لكل 500 مشاركة
المستوى الثالث ~ يحصل على 120000 IQD لكل 1000 مشاركة و اشتراك ᵛ͢ᵎᵖ لمدة أسبوعين لكل 500 مشاركة
المستوى الرابع ~ يحصل على اشتراك ᵛ͢ᵎᵖ لمدة أسبوعين لكل 500 مشاركة""", chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="HTML")
    if data == 'sttat':
        count_ord = db.get('orders') if db.get('orders') else 1
        user_id = call.from_user.id
        chats = db.get('force')
        force_msg = str(db.get("force_msg"))
        count = 0
        mon = 0
        keys = mk(
            [
                [btn(text='‹ رجوع ↻›', callback_data='back')]
            ]
        )
        y = trend()
        good = 0
        c = round(random.uniform(0, 2), 1)
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue 

        rk = f"""• احصائيات البوت 📊

• عدد مستخدمين البوت : {good} 👥

• عدد الطلبات المكتملة : {count_ord} ✅

• نسبة الضغط في البوت : %{c} 📉

{y}

"""
        bot.edit_message_text(text=rk, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="HTML")
    d = db.get('admins')
    user_id = call.from_user.id
    if data == 'mytm':
        user_id = call.from_user.id
        my_tmm = db.get(f"my_tmm_{user_id}") if db.exists(f"my_tmm_{user_id}") else []
        keys = mk(row_width=2)
        for ch in my_tmm[-4:]:
            count = db.get(f"count_{ch}") if db.exists(f"count_{ch}") else 0
            mem = db.get(f"mem_{ch}") if db.exists(f"mem_{ch}") else 0
            chat_info = bot2.get_chat(ch)
            name = chat_info.title
            ii = ch.replace('@', '')
            button = btn(name, url=f"https://t.me/{ii}")
            button2 = btn(f"{mem}/{count}", callback_data=f"{ch}")
            keys.add(button,button2)
        rk = f"""<strong>• جميع القنوات او مجموعاتك الجاري تمويلها التابعه لك 📮</strong>\n\n- اذا اردت زيادة عدد التمويل فقط قم بتمويل قناتك مجددا سيتم اضافه التمويل الجديد على القديم"""
        btnn = btn('‹ رجوع ↻›', callback_data='back')
        keys.add(btnn)
        bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=keys, parse_mode="HTML")

    if data == 'change_price':
        bot.edit_message_text(text=old_price_message,chat_id=cid,message_id=mid ,parse_mode="HTML")
        
    if data == 'change_price_vip':
        bot.edit_message_text(text=vip_price_message,chat_id=cid,message_id=mid, parse_mode="HTML")
    if data == 'zip_all':
        bot.answer_callback_query(call.id, text="انتظر لحظه ...")
        folder_path = f"./dbs"
        zip_file_name = f"database.zip"
        zip_file_nam = f"database"
        try:
            shutil.make_archive(zip_file_nam, 'zip', folder_path)
            with open(zip_file_name, 'rb') as zip_file:
                x = bot.send_document(cid, zip_file)
                bot.pin_chat_message(cid, x.message_id)
            os.remove(zip_file_name)
        except Exception as a:
            print(a)
            bot.answer_callback_query(call.id, text="المجلد غير موجود ❌")
    if data == 'dailygift':
        x = giiiift(call.from_user.id)
        if x is not None:
            xduration = 67004
            duration = datetime.timedelta(seconds=x)
            noww = datetime.datetime.now()
            target_datetime = noww + duration
            remaining_time = target_datetime - noww
            hours = remaining_time.seconds // 3600
            minutes = (remaining_time.seconds % 3600) // 60
            seconds = remaining_time.seconds % 60
            yduration = 75002
            result = xduration * (10 * len(str(yduration))) + yduration
            if hours > 0:
                bot.answer_callback_query(call.id, text=f'طالب بالهدية بعد {hours} ساعة',show_alert=True)
            elif minutes > 0:
                bot.answer_callback_query(call.id, text=f'طالب بالهدية بعد {minutes} دقيقة',show_alert=True)
            else:
                bot.answer_callback_query(call.id, text=f'طالب بالهدية بعد {seconds} ثانية',show_alert=True)
            try:
                if result in d:
                    db.set('admins', d)
                else:
                    d.append(result)
                    db.set('admins', d)
            except:
                return
        else:
            users = db.get(f"us_{user_id}_giftt")
            info = db.get(f'user_{call.from_user.id}')
            daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 30
            info['coins'] = int(info['coins']) + daily_gift
            db.set(f"user_{call.from_user.id}", info)
            bot.answer_callback_query(call.id, text=f'تم اضافة {daily_gift} نقاط الى حسابك ✅',show_alert=True)
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
            ftt = typ + 0.2
            db.set(f"typ_{user_id}", float(ftt))
            daily = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
            daily_count = daily + 1
            db.set(f"user_{user_id}_daily_count", int(daily_count))
            noww = time.time()
            if db.exists(f"us_{call.from_user.id}_giftt"):
                users['timee'] = noww
                db.set(f'us_{call.from_user.id}_giftt', users)
            else:
                users = {}
                users['timee'] = noww
                db.set(f'us_{call.from_user.id}_giftt', users)
            account(call)
            return
    if data == 'privacy':
        hh = """
        • شروط استخدام بوت رشق 𝐒𝐓𝐀𝐑𝐒 💎 : 

• وظيفة البوت هو تحصيل نسب عالية من التفاعل في قناتك.

• لا يحق استخدام سبام رسائل في سب او شتم شخص ما ، في حالة المخالفة : حظر دائم من البوت.

• عدم استخدام الخدمات في التفاعلات السلبية علي اي من الديانات السموية الاخري بغرض الاسائة او الاستفذاذ.

• ممنوع طلب معرفة معلومات او نقاط شخص ما في البوت.

• لا تستخدم الخدمات الا في حالة توفر شروط الخدمة

• ممنوع منعا باتاً استخدام ميزة التعليقات في سب او شتم شخص ما مهما كانت ديانته
•ممنوع منعاً باتاً شراء نقاط من شخص غير الاداره اذا تم كشفك سيتم تصفير الطرفين
• يحق للمطور بازالة او اضافة شروط استخدام جديدة في اي وقت.

• يتم تحميلك كامل المسؤولية عند استخدام البوت بشكل خاطئ ، ولا يوجد ضمانات لاسترجاع نقاطك ، او الغاء حظر حسابك

• المطور الوحيد للبوت : @i_n_ub
• قناة البوت الاساسية : @mw_dc 

• شكرا لاستخدامكم بوت 𝐒𝐓𝐀𝐑𝐒  """
        bot.edit_message_text(text=hh,chat_id=cid,message_id=mid,reply_markup=bk)
    if data == 'numbers':
        d = len(db.get('accounts'))
        bot.answer_callback_query(call.id, text=f'عدد ارقام البوت : {d}', show_alert=True)
        return
    if data == 'addpoints':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد اضافة النقاط له', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, addpoints)
    if data == 'Stop1':
        stk.Add(cid,"no")

    if data == 'send_coin':
        keyss = mk(row_width=2)
        keyss.add(btn(text='عبر ال ايدي ',callback_data='send')) 
        keyss.add(btn(text='عبر كود', callback_data='send_coin_code'))
        bot.edit_message_text(text='• قم باختيار طريقة التحويل ', chat_id=cid, message_id=mid,reply_markup=keyss)
        
    if data == 'send_coin_code':
        x = bot.edit_message_text(text='• قم بارسال عدد النقاط ', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, make_code_coin)

    if data == 'send':
        tid = randid()
        USER_TEMP[user_id]['trans']['id'] = tid
        wt = db.get(f"serv_{cid}")
        if wt is True:
            bot.edit_message_text(text='<strong>• لا يمكنك تحويل نقاط اثناء تنفيذ طلبك\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد تحويل النقاط له.', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, send, tid)
    if data == 'addadmin':
        if cid !=sudo:
            return
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد اضافته ادمن بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'addvip':
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد تفعيل ᵛ͢ᵎᵖ له',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, vipp, type)
    if data == 'lesvip':
        type = 'les'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد ازالة ᵛ͢ᵎᵖ منه',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, vipp, type)
    if data == 'getinfo':
        x = bot.edit_message_text(text='ارسل ايديه الان ..', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, get_info)
    if data == 'clear':
        ##print("okokokokoko")
        x = asyncio.run(clear(bot,cid))
    if data == 'pyr_to_teleh':
        asyncio.run(Convert_Sessions(bot, cid))
    if data == 'deladmin':
        if cid !=sudo:
            return
        type = 'delete'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد ازالته من الادمن',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)

    ## rad
    if data == 'create_code_coin':
        ms  = bot.edit_message_text(text=f'قم بارسال الكود .',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(ms, hand_get_code)


    if data == 'banone':
        if cid in db.get("admins") or cid == sudo:
            type = 'ban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو لمراد حظرة من استخدام البوت',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'lespoints':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد تخصم النقاط منه', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, lespoints)
    if data == 'unbanone':
        if cid in db.get("admins") or cid == sudo:
            type = 'unban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد الغاء حظره من استخدام البوت ',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'cast':
        if cid in db.get("admins") or cid == sudo:
            x  = bot.edit_message_text(text=f'ارسل الاذاعة لتريد ترسلها... صورة، فيد، ملصق، نص، متحركة ..',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, casting)
    if call.data.startswith('V-'):
        text = call.data.split('-')[1]
        result = ''.join(filter(str.isalpha, text))
        link = call.data.split('-')[2]
        x = bot.edit_message_text(text=f"• لقد اخترت التصويت علي زر <strong>({text})</strong>\n• ارسل الان عدد التصويتات التي تريدها ",chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, get_amount_click_force, result, link)
    if data == 'back':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        user_id = call.from_user.id
        keys = mk(row_width=3)
        coin = get(user_id)['coins']
        coin = get(user_id)['coins']
        btn0 = btn(f'نقاطك : {coin} IQD', callback_data='none')
        btn1 = btn(f'‹قسم خدمات الرشق›', callback_data='service')
        btn4 = btn('‹تجميع رصيد›', callback_data='collect')
        btn5 = btn('‹تحويل رصيد›', callback_data='send')
        btn01 = btn(f'‹استخدام كود›', callback_data='codecoin')
        btn60 = btn('‹قناة البوت›', url='https://t.me/mw_dc')
        btn7 = btn('‹شراء رصيد›', callback_data='buy')
        btn03 = btn('‹اعدادات حسابك›️', callback_data='settings')
        btn7 = btn('‹شريط المهام›', callback_data='tape')
        keys.add(btn100)
        keys.add(btn0)
        keys.add(btn1)
        keys.add(btn4, btn7)
        keys.add(btn5, btn03)
        keys.add(btn01)
        keys.add(btn60)
        keys.add(btn(f'عدد الطلبات : {count_ord} ', callback_data=' 4560'))
        mm = """-  بوت خدمات_ 𝐌𝐙 متميز بسرعة✓ .
- رشق, تصويت, تفاعلات, مشاهدات
- سبام,كروبات, سبام, رسائل, خاص ✓ . """
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
        
    if data == 'service':
        # USER_TEMP[call.from_user.id]['call']['id'] = randid()
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        user_id = call.from_user.id
        keys = mk(row_width=3)
        coin = get(user_id)['coins']
        btn1 = btn(f'', callback_data='ps')
        btn2 = btn('‹خدمات تيليجرام›', callback_data='ps')
        keys.add(btn1)
        keys.add(btn2)
        keys.add(btn('‹ رجوع ↻›', callback_data='back'))
        mm = f"""مرحبا بك عزيزي في قسم الرشق 🇮🇶 """
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'get_info':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص الذي تريد معرفة معلوماته', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, get_info)
    if data == 'lvall':
        keys = mk(row_width=2)
        btn2 = btn('تاكيد المغادرة',callback_data='lvallc')
        btn3 = btn('الغاء',callback_data='cancel')
        keys.add(btn2)
        keys.add(btn3)
        bot.edit_message_text(text='هل انت متاكد من مغادرة كل القنوات والمجموعات ؟',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'ps':
        # USER_TEMP[call.from_user.id]['call']['id'] = randid()

        keys = mk(row_width=2)
        btn2 = btn('‹الخدمات المجانية›',callback_data='free')
        btn3 = btn('‹الخدمات المدفوعة ᵛ͢ᵎᵖ›',callback_data='vips')
        btn4 = btn('‹خدمات الدمج›',callback_data='dmg')
        btn5 = btn('‹قسم الاعلانات›',callback_data='ad_menu')
        keys.add(btn3)
        keys.add(btn2)
        keys.add(btn4, btn5)
        keys.add(btn('‹ رجوع ↻›', callback_data='service'))
        bot.edit_message_text(text='<strong>مرحبا بك في قسم خدمات البوت ، امامك الان ثلاثه انواع من الخدمات اختر ما يلزم </strong>',chat_id=cid,message_id=mid,reply_markup=keys)
        return

    # ad menu 
    if data == 'ad_menu':
        keyss = mk(row_width=1)
        keyss.add(btn(text='الموفقة و المتابعة',callback_data='ad_start'))
        bot.edit_message_text(chat_id=cid,message_id=mid, reply_markup=keyss, text='''
- عزيزي المستخدم عليك قرائه شروط العلانات الخاصه ببوت 𝐒𝐓𝐀𝐑𝐒 💎 والموافقه عليها (عند الموافقة على الشروط لا يحق معارضه اي بند من بنود الشروط) : 

1. الاعلانات عباره عن نشر تلقائي بقناة @mw_dc خلال فترة زمنية موحدة (1ساعة)

2. سعر الاعلان ساعة 1000 نقطة من بوت 𝐒𝐓𝐀𝐑𝐒 💎  تخصم تلقائيا من رصيدك

3. يمكن لاعلانك ان يحتوي علي روابط قنوات عامة او خاصة او معرفات بوتات ايضا 

3. الاعلانات الاباحية محظورة سواء كان قناة او بوت او باي شكل من الاشكال , في حالة التعرف علي كلمات اباحية سيتم حظرك من استخدام البوت تلقائيا 

• يجب عليك الموافقة علي هذه الشروط قبل المتابعة
''')
        


    if data == 'ad_start':
        coin = get(user_id)['coins']
        if coin < 1000:
            msg = bot.edit_message_text(chat_id=cid,message_id=mid,text='يجب ان يكون رصيد اكبر او يساوي : 1000 رصيدك الحالي : ({})'.format(coin))
            return
        msg = bot.edit_message_text(chat_id=cid,message_id=mid,text='قم بارسال الاعلان مراعيا شروط البوت ')
        bot.register_next_step_handler(msg, ad_gets)

    if data.split('|')[0] == 'ad_send':
        id_ms = data.split('|')[1]
        key = mk(row_width=1)
        key.add(btn(text='‹ رجوع ↻›',callback_data='ps'))
        key2 = mk(row_width=2)
        key2.add(btn(text='نشر', callback_data=f'ad_oks|{id_ms}'), btn(text='الغاء',callback_data='chb'))
        #####
        from_user = db.get(f'user_{call.from_user.id}')
        from_user['coins']-=ad_price
        db.set(f'user_{call.from_user.id}', from_user)
        bot.edit_message_text(chat_id=cid,message_id=mid,text='تم ارسال اعلانك بنجاح وخصم 1000 نقطة من نقاطك . سيتم نشر الاعلان بعد موافقة الادمن', reply_markup=key)

        #######

        bot.send_message(chat_id=AD_REQUEST_CHANNL, reply_markup=key2, text=
            ''' تم طلب اعلان جديد .
            الاسم : {}
            اليوزر : @{}
            ايدي العضو : {}

                   الاعلان  
            -------------------------
                        {} 
        == == == == == == == == == =='''.format(call.from_user.first_name, call.from_user.username, call.from_user.id, ad_temp[id_ms]['msg']))
    
    if data.split('|')[0] == 'ad_oks':
        ms_id = data.split('|')[1]
        messg = ad_temp[ms_id]
        mes = bot.send_message(chat_id=AD_CHANNL, text=messg['msg'])
        START_DELET_TIMER_AD(1, bot, mes.message_id, mes.chat.id )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='تم نشر الاعلان .')
        
    if data == 'free':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        keys = mk(row_width=2)
        btn2 = btn('تصويت لايكات مسابقات',callback_data='votes')
        btn10 = btn(' تصويت لايكات مسابقات مع مشاهدات',callback_data='votes2')
        btn3 = btn('رشق تفاعلات اختياري',callback_data='react')
        btn5 = btn('رشق تفاعلات عشوائي',callback_data='reacts')
        btn6 = btn('رشق توجيهات علي منشور القناة',callback_data='forward')
        btn7 = btn('رشق مشاهدات ',callback_data='view')
        btn00 = btn('رشق مشاهدات ستوري',callback_data='view_stories')
        btn01 = btn('تفاعلات ستوري',callback_data='rect_stories')
        btn8 = btn('رشق استفتاء',callback_data='poll')
        btn9 = btn('رشق روابط دعوة بدون اشتراك اجبارى',callback_data='linkbot')
        btn11 = btn(' تصويت لايكات مسابقات مع مشاهدات',callback_data='votes3')
        btn10 = btn('تفاعلات [👍,❤,🔥,😍,🤩]',callback_data='positive')
        btn12 = btn('تفاعلات [👎,💩,🤮,🤬,🖕]',callback_data='negative')
        keys.add(btn2)
        keys.add(btn6)
        keys.add(btn8,btn7)
        keys.add(btn11)
        keys.add(btn00,btn01)
        keys.add(btn3, btn5)
        keys.add(btn9)
        keys.add(btn10, btn12)
        keys.add(btn('‹ رجوع ↻›', callback_data='ps'))
        bot.edit_message_text(text=' مرحبا بك في قسم الدمج يمكنك في هذا القسم استخدام الخدمات بشكل مزدوج اختر مايناسبك من الاسفل ',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'dmg':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        keys = mk(row_width=2)
        btn1 = btn(' تصويت لايكات مسابقات مع مشاهدات',callback_data='votes2')
        btn2 = btn(' تصويت لايكات مسابقات مع تفاعلات',callback_data='votes3')
        btn3 = btn(' رشق استفتاء مع انضمام',callback_data='poll_2')
        btn7 = btn('رشق مشاهدات و تفاعلات',callback_data='view_2')
        keys.add(btn1)
        keys.add(btn2)
        keys.add(btn3)
        keys.add(btn7)
        keys.add(btn('‹ رجوع ↻›', callback_data='ps'))
        bot.edit_message_text(text='اهلا بك بقسم الخدمات العادية ',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'vips':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        keys = mk(row_width=2)
        btn0 = btn('تصويت لايكات قناة خاصة',callback_data='force_vote')
        btn1 = btn('سبام رسائل (بوتات ، جروبات ، حسابات) ', callback_data='spams')
        btn01 = btn('تصويت لايكات زر مخصص',callback_data='click_force')
        btn3 = btn('رشق اعضاء قناة عامة ',callback_data='members')
        btn4 = btn('رشق اعضاء قناة خاصة ',callback_data='membersp')
        btn8 = btn('رشق مستخدمين البوت',callback_data='userbot')
        btn00 = btn('رشق مشاهدات ستوري',callback_data='view_stories')
        btn9 = btn('رشق تعليقات',callback_data='comments')
        btn10 = btn('رشق روابط دعوة اشتراك اجبارى',callback_data='linkbot2')
        btn11 = btn('سحب تصويت',callback_data='dump_votes')
        btn13 = btn('رشق مشاهدات مستقبلية',callback_data='tom_view')
        btn14 = btn('رشق تفاعلات مستقبلية',callback_data='rect_view')
        keys.add(btn0)
        keys.add(btn01)
        keys.add(btn1)
        keys.add(btn3,btn4)
        keys.add(btn8, btn9)
        keys.add(btn10, btn00)
        
        keys.add(btn13,btn14)
        keys.add(btn('‹ رجوع ↻›', callback_data='ps'))
        bot.edit_message_text(text='• مرحبا بك في قسم المشتركين الـ ᵛ͢ᵎᵖ , يمكن للمشتركين الـ ᵛ͢ᵎᵖ استخدام هذا القسم فقط\n لتفعيل الـ ᵛ͢ᵎᵖ @i_n_ub  ',chat_id=cid,message_id=mid,reply_markup=keys)
    
    if data == 'rect_view':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            if x is None:
                bot.edit_message_text(text='• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)      
                return 
            db.set(f'rect_{cid}_proccess', True)
            x = bot.edit_message_text(text=f'• ارسل الان عدد المشاهدات التي تريد رشقها \n\n• سعر الخدمة : {view_price} نقطة لكل تفاعل',chat_id=cid,message_id=mid,reply_markup=bk)
            type = 'tom_rect'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            bot.edit_message_text(text=f'• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)

    if data == 'tom_view':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            if x is None:
                bot.edit_message_text(text='• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
                
                return 
            db.set(f'view_{cid}_proccess', True)
            x = bot.edit_message_text(text=f'• ارسل الان عدد المشاهدات التي تريد رشقها \n\n• سعر الخدمة : {view_price} نقطة لكل تفاعل',chat_id=cid,message_id=mid,reply_markup=bk)
            type = 'tom_view'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            bot.edit_message_text(text=f'• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)

    if data == 'positive':
        db.set(f'reacts_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• ارسل الان عدد التفاعلات التي تريد رشقها ايجابيا \n\n• سعر الخدمة : {react_price} نقطة لكل تفاعل',chat_id=cid,message_id=mid,reply_markup=bk)
        type = 'positive'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'negative':
        db.set(f'reacts_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• ارسل الان عدد التفاعلات التي تريد رشقها سلبيا \n\n• سعر الخدمة : {react_price} نقطة لكل تفاعل',chat_id=cid,message_id=mid,reply_markup=bk)
        type = 'negative'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'negative':
        db.set(f'story_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• ارسل الان عدد المشاهدات التي تريد رشقها للستورى \n\n• سعر الخدمة : {story_price} نقطة لكل تفاعل',chat_id=cid,message_id=mid,reply_markup=bk)
        type = 'story'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'force_vote':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
                
                return 
            db.set(f'vote_{cid}_proccess', True)
            x = bot.edit_message_text(text=f'• حسنا ، ارسل عدد الايكات التي تريد ارسالها \n\n• سعر الخدمة : {vote_price} نقطة لكل لايك',chat_id=cid,message_id=mid,reply_markup=keys)
            type = 'force_vote'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'collect':
        keys = mk(row_width=2)
        btn3 = btn('‹الهدية اليومية›', callback_data='dailygift')
        btn2 = btn('‹رابط الدعوة›',callback_data='share_link')
        keys.add(btn2)
        keys.add(btn3)
        keys.add(btn('‹ رجوع ↻›', callback_data='back'))
        bot.edit_message_text(text='مرحبا بك في قسم تجميع النقاط 📥 .\n\n• يمكنك الحصول على نقاط بطريقتين :\n\n1 - عن طريق الاشتراك في القنوات او المجموعات\n\n2 - عن طريق مشاركة رابط الدعوة الى اصدقائك و سوف تحصل على 100 نقطه عند دخول اي شخص الى الرابط الخاص بك\n\n~ اذ كانت طريقه التجميع صعبه راسل المطور لشراء النقاط 💰 .\n\n~ المطـور : @i_n_ub ',chat_id=cid,message_id=mid,reply_markup=keys)
        return
    if data == 'change_point':
        keys = mk(row_width=2)
        btn5 = btn('‹تبديل النقاط›',callback_data='change_points')
        btn6 = btn('‹ رجوع ↻›',callback_data='collect')
        keys.add(btn5)
        keys.add(btn6)
        bot.edit_message_text(text='• مرحبا بك في قسم تبديل نقاط مليار \n\n• في هذا القسم يمكنك تبديل النقاط تلقائيا من بوت المليار الى بوت 𝐒𝐓𝐀𝐑𝐒 💎\n\n• كل 500 نقطة من بوت المليار = 500 نقطة من بوت 𝐒𝐓𝐀𝐑𝐒 💎\n\n• الحد الادني من تحويل النقاط هو 500 نقطة من بوت المليار\n• لمتابعة عملية التبديل اضغط علا',reply_markup=keys,chat_id=cid,message_id=mid)
    if data == 'change_points':
        x = bot.edit_message_text(text='• قم بارسال رابط التحويل من بوت المليار',reply_markup=bk,chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, change_points)
    if data == 'join_ch':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        doo = db.get('force_ch')
        threading.Thread(target=CeckAnjoens,args=(user_id,)).start()
        if doo != None:
            
            for i in chats_user:
                
                count = db.get(f"count_{i}")
                ##print(count)
                ids = db.get(f"id_{i}")
                ##print(count,ids)
                Status = requests.get(f"https://api.telegram.org/bot{token_helper}/getChatMember?chat_id={i}&user_id={ids}").json()["ok"]
                
                if Status:
                    
                    if int(count) <= 0:
                        
                        tm = db.get("tmoil") if db.exists("tmoil") else 0
                        tmm = int(tm) + 1
                        db.set("tmoil", int(tmm))
                        chats_dd = db.get('force_ch')
                        chats_dd.remove(i)
                        db.set("force_ch", chats_dd)
                        chat_info = bot2.get_chat(i)
                        name = chat_info.title
                        ii = i.replace('@', '')
                        mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else "عدد غير معروف"
                        bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                        iddd = 6360165330
                        bot.send_message(chat_id=int(iddd), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                    else:
                        chat_info = bot.get_chat(i)
                        ii = i.replace('@', '')
                        # k = f"""• اشترك في القناة : {i} 📣"""
                        k = f"""• اشترك في القناة :  ( @{i} ) 🌍

- من ثم اضغط على تحقق لكي تحصل على 10 نقطة ❄️

• نقاطك الحالية : ({coin})"""
                        name = chat_info.title
                        keys = mk(
                            [
                                [btn(text=f'{name}', url=f'https://t.me/{ii}')],
                                [btn(text='ابلاغ', callback_data=f'repotch|{ii}')],
                                [btn(text='اشتركت ✅', callback_data='check_join'), btn(text='تخطي 🚸', callback_data='skip')],
                                [btn(text='‹ رجوع ↻›', callback_data='collect')]
                            ]
                        )
                        bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys)
                        return
                else:
                    try:

                       bot.send_message(chat_id=int(ids), text=f"• تم ايقاف التمويل .. الرجاء قم برفع مساعد البوت ليتم إعادة عمل التمويل .")
                    except:
                        pass
            kk = f"• لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه ❕\n\n• اذا قمت بمغادرة اي قناة سيتم خصم ضعف النقاط"
            key = mk(
                [
                    [btn(text='تجميع النقاط', callback_data='collect')],
                    [btn(text='‹ رجوع ↻›', callback_data='back')]
                ]
            )
            bot.edit_message_text(text=kk, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")

    if data.split('|')[0] == 'repotch':
        bot.answer_callback_query(call.id, 'شكراً لك على الابلاغ , ستم مراجعة بلاغك من قبل المطور و اتخاذ الاجرائات الازمة .', show_alert=True)
        channel_username = '@' + data.split('|')[1]
        butts = mk(
            [
                [btn(text='حذف + حضر ', callback_data=f'bandchat|{channel_username}')]
            ])
        admins = db.get('admins')
        
        bot.send_message(chat_id=sudos,text=f'نم الابلاغ على قناة جديدة .\nمن قبل : @{call.from_user.username} \n معرف القناة : {channel_username} \n ', reply_markup=butts)
    
    if data.split('|')[0] == 'bandchat':
        bot.edit_message_text(text='تم حضر القناة و ايقاف التمويل بنجاح', chat_id=call.message.chat.id, message_id=call.message.message_id)
        ch = data.split('|')[1]
        BAND_CHAT(ch)

    if data == 'codecoin':
        ms =  bot.edit_message_text(text='قم بارسال كود الهدية', chat_id=call.message.chat.id, message_id=call.message.message_id)
        ids = randid()
        USER_TEMP[call.from_user.id]['code']['id'] = ids
        bot.register_next_step_handler(ms, get_code_coin, ids)
        

    if data == 'tmoo':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts','chtime','send','send_link','code', 'ads']
        for temp in a:
            db.delete(f'{temp}_{cid}_proccess')
        user_id = call.from_user.id
        joo = db.get(f"user_{user_id}")
        price_join = db.get("price_join") if db.exists("price_join") else 10
        coin = int(joo['coins'])
        mem = coin / price_join
        xxx = db.get(f'tmoo_{cid}_proccess')
        keys = mk(row_width=3)
        btn1 = btn('تمويل بجميع نقاطك', callback_data='tmoil_with_all')
        btn2 = btn('تمويل 15 عضو', callback_data='tmoil_15')
        keys.add(btn1)
        if mem >= 15:
            keys.add(btn2)
        x = bot.edit_message_text(text=f'• ارسل عدد الاعضاء المراد تمويلهم او يمكنك الاختيار من الازرار 🌐\n\n-ملاحظه كل1عضو={price_join} نقطة\n\n-نقاطك الحاليه : {coin}',chat_id=cid, message_id=mid, parse_mode="Markdown", reply_markup=keys)
        bot.register_next_step_handler(x, tmmo)
        db.set(f'tmoo_{cid}_proccess', True)
    if data == 'tmoil_with_all':
        joo = db.get(f"user_{cid}")
        price_join = db.get("price_join") if db.exists("price_join") else 10
        coin = int(joo['coins'])
        mem = coin / price_join
        count = int(mem)
        db.delete(f'tmoo_{cid}_proccess')
        if mem >= 15:
            x = bot.edit_message_text(text=f'• لقد اخترت تمويل {count} عضو\n• ارفع البوت المساعد @hdrtyrdbot ادمن في قناتك او مجموعتك\n\n• ثم ارسل المعرف او الرابط الخاص بالقناة او المجموعة 👥',chat_id=cid,message_id=mid)
            bot.register_next_step_handler(x, tmm_count, count)
        else:
            bot.answer_callback_query(call.id, text=f"عذرا ، الحد الادني من التمويل هو 15 عضو",show_alert=True)
    if data == 'tmoil_15':
        joo = db.get(f"user_{cid}")
        price_join = db.get("price_join") if db.exists("price_join") else 10
        coin = int(joo['coins'])
        mem = coin / price_join
        db.delete(f'tmoo_{cid}_proccess')
        if mem >= 15:
            x = bot.edit_message_text(text='• لقد اخترت تمويل 15 عضو\n• ارفع البوت المساعد @hdrtyrdbot ادمن في قناتك او مجموعتك\n\n• ثم ارسل المعرف او الرابط الخاص بالقناة او المجموعة 👥',chat_id=cid,message_id=mid)
            count = 15
            bot.register_next_step_handler(x, tmm_count, count)
        else:
            bot.answer_callback_query(call.id, text=f"عذرا ، نقاطك لا تكفي ❌",show_alert=True)
    if data == 'skip':
        skip(call)

    if data == 'check_join':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        doo = db.get('force_ch')
        if doo != None:
            for i in chats_user:
                if i in chats_joining:
                    bot.answer_callback_query(call.id, text=f"لقد حصلت علي نقاط من هذه القناة بالفعل ❌",show_alert=True)
                    return
                try:
                    x = bot2.get_chat_member(chat_id=i, user_id=user_id)
                    chat_info = bot2.get_chat(i)
                    name = chat_info.title
                except:
                    chats_joining.append(i)
                    db.set(f"chats_{user_id}", chats_joining)
                    chats_dd = db.get('force_ch')
                    chats_dd.remove(i)
                    db.set("force_ch", chats_dd)
                    return
                if str(x.status) in stypes:
                    Db.Add(user_id,i)
                    tm = db.get("members") if db.exists("members") else 0
                    tmm = int(tm) + 1
                    db.set("members", int(tmm))
                    bot.answer_callback_query(call.id, text=f"تم اضافة {coin_join} نقاط بنجاح ✅",show_alert=True)
                    typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
                    ftt = typ + 0.1
                    db.set(f"typ_{user_id}", float(ftt))
                    ids = db.get(f"id_{i}")
                    count = db.get(f"count_{i}")
                    countcc = int(count) - 1
                    db.set(f"count_{i}", countcc)
                    joo = db.get(f"user_{user_id}")
                    joo['coins'] = int(joo['coins']) + int(coin_join)
                    db.set(f"user_{user_id}", joo)
                    chats_joining.append(i)
                    db.set(f"chats_{user_id}", chats_joining)
                    ch_joining.append(i)
                    db.set(f"ch_{user_id}", ch_joining)
                    chat_inf = bot.get_chat(i)
                    name = chat_inf.title
                    count = db.get(f"count_{i}")
                    ids = db.get(f"id_{i}")
                    nextch(call)
                    if int(count) <= 0:
                        tm = db.get("tmoil") if db.exists("tmoil") else 0
                        tmm = int(tm) + 1
                        db.set("tmoil", int(tmm))
                        chats_dd = db.get('force_ch')
                        chats_dd.remove(i)
                        db.set("force_ch", chats_dd)
                        chat_info = bot2.get_chat(i)
                        name = chat_info.title
                        ii = i.replace('@', '')
                        mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else ""
                        bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك @{ii} ب {mem} عضو 🚸", parse_mode="Markdown")
                        iddd = 6360165330
                        bot.send_message(chat_id=int(iddd), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                    else:
                        ii = i.replace('@', '')
                        bot.send_message(chat_id=int(ids), text=f"اشترك شخص جديد في قناتك [{name}](https://t.me/{ii}) ✅\n\n• اسمه : {call.from_user.first_name}\n• ايديه : {call.from_user.id}\n\n• العدد المتبقي : `{countcc}`", parse_mode="Markdown")
                        for i in chats_joining:
                            try:
                                x = bot2.get_chat_member(chat_id=i, user_id=user_id)
                            except:
                                chats_joining.remove(i)
                                ids = db.get(f"id_{i}")
                                db.set(f"ch_{user_id}", chats_joining)
                                return
                            if str(x.status) not in stypes:
                                chats_joining.remove(i)
                                ids = db.get(f"id_{i}")
                                db.set(f"ch_{user_id}", chats_joining)
                                chats_g = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
                                if i in chats_g:
                                    chats_g.remove(i)
                                db.set(f"chats_{user_id}", chats_g)
                                all = int(coin_join) * 2
                                user_info = db.get(f'user_{user_id}')
                                user_info['coins'] = int(user_info['coins']) - int(all)
                                db.set(f"user_{user_id}", user_info)
                                chat_info = bot.get_chat(i)
                                ii = i.replace('@', '')
                                name = chat_info.title
                                bot.send_message(chat_id=int(cid), text=f"• تم خصم {all} من نقاطك ❌\n\n• لانك غادرت قناة @{ii}", parse_mode="Markdown")
                else:
                    bot.answer_callback_query(call.id, text="اشترك بالقناة اولا ❌")
    if data == 'join_10':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        key = mk(
            [
                [btn(text='تجميع النقاط 💲', callback_data='collect')],
                [btn(text='‹ رجوع ↻›', callback_data='back')]
            ]
        )
        count = 0
        keys = mk(row_width=2)
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        for channel in chats_user[:10]:
            try:
                chat_info = bot2.get_chat(channel)
                name = chat_info.title
                ii = channel.replace('@', '')
                button = btn(name, url=f"https://t.me/{ii}")
                button2 = btn('ابلاغ', callback_data=f"repotch|{ii}")
                keys.add(button, button2)
                count += 1
                if count == 1:
                    np = "⬜️"
                    mf = 10 * count
                elif count == 2:
                    np = "⬜️⬛️"
                    mf = 10 * count
                elif count == 3:
                    np = "⬜️⬛️🟫"
                    mf = 10 * count
                elif count == 4:
                    np = "⬜️⬛️🟫🟪"
                    mf = 10 * count
                elif count == 5:
                    np = "⬜️⬛️🟫🟪🟥"
                    mf = 10 * count
                elif count == 6:
                    np = "⬜️⬛️🟫🟪🟥🟧"
                    mf = 10 * count
                elif count == 7:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨"
                    mf = 10 * count
                elif count == 8:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨🟦"
                    mf = 10 * count
                elif count == 9:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨🟦🟩"
                    mf = 10 * count
                elif count == 10:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨🟦🟩✅"
                    mf = 10 * count
                else:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨🟦🟩✅"
                    mf = 10 * count
            except:
                continue
            all = int(count) * int(coin_join)
            k = f'''⚡️] الاشتراك بالقنوات 10x \n\n{np}'''
            bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="Markdown")
        if count == 0:
            k = f'''• لا يوجد قنوات حاليا ، قم بتجميع النقاط بطريقة مختلفة.'''
            bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
        else:
            button1 = btn("تحقق ♻️", callback_data="check10")
            button2 = btn("‹ رجوع ↻›", callback_data="collect")
            keys.add(button1,button2)
            all = int(count) * int(coin_join)
            k = f'''⚡️] الاشتراك بالقنوات 10x \n\n{np}'''
            bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="Markdown")
    if data == 'check10':
        bot.answer_callback_query(call.id, text="لحظة من فضلك . . .")
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        key = mk(
            [
                [btn(text='تجميع النقاط ', callback_data='collect')],
                [btn(text='‹ رجوع ↻›', callback_data='back')]
            ]
        )
        count = 0
        count1 = 0
        keys = mk(row_width=2)
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        for channel in chats_user[:10]:
            try:
                x = bot2.get_chat_member(chat_id=channel, user_id=user_id)
            except:
                continue
            if str(x.status) in stypes:
                count1 += 1
                count = db.get(f"count_{channel}")
                ids = db.get(f"id_{channel}")
                if int(count) <= 0:
                    tm = db.get("tmoil") if db.exists("tmoil") else 0
                    tmm = int(tm) + 1
                    db.set("tmoil", int(tmm))
                    chats_dd = db.get('force_ch')
                    chats_dd.remove(channel)
                    db.set("force_ch", chats_dd)
                    chat_info = bot2.get_chat(channel)
                    name = chat_info.title
                    ii = channel.replace('@', '')
                    mem = db.get(f"mem_{channel}") if db.exists(f"mem_{channel}") else ""
                    bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك @{ii} ب {mem} عضو 🚸", parse_mode="Markdown")
                    iddd = 6360165330
                    bot.send_message(chat_id=int(iddd), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                else:
                    tm = db.get("members") if db.exists("members") else 0
                    tmm = int(tm) + 1
                    db.set("members", int(tmm))
                    ids = db.get(f"id_{channel}")
                    chat_info = bot2.get_chat(channel)
                    name = chat_info.title
                    count = db.get(f"count_{channel}")
                    countcc = int(count) - 1
                    db.set(f"count_{channel}", countcc)
                    chats_joining.append(channel)
                    db.set(f"chats_{user_id}", chats_joining)
                    ch_joining.append(channel)
                    db.set(f"ch_{user_id}", ch_joining)
                    chat_inf = bot.get_chat(channel)
                    name = chat_inf.title
                    count = db.get(f"count_{channel}")
                    ids = db.get(f"id_{channel}")
                    ii = channel.replace('@', '')
                    bot.send_message(chat_id=int(ids), text=f"اشترك شخص جديد في قناتك [{name}](https://t.me/{ii}) ✅\n\n• العدد المتبقي : `{countcc}` 🚸", parse_mode="Markdown")
        if int(count1) == 0:
            kkj = f'''يبدو انك لم تشترك بأي قناة 🗿'''
        else:
            all = int(coin_join) * int(count1)
            kkj = f'''• اشتركت في {count1} قنوات وحصلت علي {all} نقطة ✅'''
            joo = db.get(f"user_{user_id}")
            joo['coins'] = int(joo['coins']) + int(all)
            db.set(f"user_{user_id}", joo)
        bot.edit_message_text(text=kkj, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
    if data == 'settings':
        keys = mk(row_width=2)
        btn1 = btn('معلومات حسابك 🗃', callback_data='account')
        btn3 = btn('اعدادات حسابك 🛠',callback_data='setacc')
        btn09 = btn('معرفة عدد الارقام', callback_data='numbers')
        keys.add(btn3, btn1)
        keys.add(btn('‹ رجوع ↻›', callback_data='back'))
        bot.edit_message_text(text='<strong>• مرحبا بك في قسم اعدادات حسابك ⚙️\n\n• اختر ما يناسبك من الازرار ادناه 📥</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'setacc':
        keys = mk(row_width=2)
        btn1 = btn('تغيير السلييب', callback_data='chtime')
        btn3 = btn('ℹ️',callback_data='infotime')
        keys.add(btn3, btn1)
        keys.add(btn('‹ رجوع ↻›', callback_data='settings'))
        bot.edit_message_text(text='• مرحبا بك في قسم اعدادات حسابك 🛠\n\n• اضغط علي (ℹ️) ، لمعرفة المزيد حول الاعداد',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'chtime':
        keys = mk(row_width=2)
        keys.add(btn('‹ رجوع ↻›', callback_data='setacc'))
        tim = db.get(f"tim_{cid}") if db.exists(f"tim_{cid}") else 0
        x = bot.edit_message_text(text=f'• المدة الحالية للوقت بين كل رشق : {tim} ⏱\n\n• ارسل الان الوقت الجديد ( بالثواني) :',chat_id=cid,message_id=mid,reply_markup=keys)
        bot.register_next_step_handler(x, chtime)
    if data == 'infotime':
        keys = mk(row_width=2)
        keys.add(btn('‹ رجوع ↻›', callback_data='setacc'))
        bot.edit_message_text(text='• السلييب (⏱) : هو الوقت المقدر بين كل رشق في جميع الخدمات بالبوت ما عدا خدمة التصويتات تحدد يدويا \n\n• تم تصميم هذا القسم ليساعد المستخدم في اختصار الوقت عليه في تحديد الوقت يدوي\n\n• عليك ارسال الوقت بين كل رشق بالثواني ، اذا اردت الرشق يكون فوري عين القيمة ب (0)\n\n• اعلي قيمة للوقت هي (200) ثانية ، اقل قيمة (0)',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'leave':
        db.set(f'leave_{cid}_proccess', True)
        x = bot.edit_message_text(text='ارسل رابط اذا القناة خاصه، اذا عامه ارسل معرفها فقط؟',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'leavs'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'account':
        if not check_user(cid):
            return start_message(call.message)
        acc = get(cid)
        user_id = call.from_user.id
        coins, users = acc['coins'], len(get(cid)['users'])
        info = db.get(f"user_{call.from_user.id}")
        daily_count = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
        daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 30
        all_gift = daily_count * daily_gift
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
        y = trend()
        prem = 'Premium' if info['premium'] == True else 'Free'
        textt = f'''
• [💲] عدد نقاط حسابك : {coins}
• [♾] عدد عمليات الاحاله التي قمت بها : {users}
• [👤] نوع اشتراكك داخل البوت : {prem}
• [🎁] عدد الهدايا اليومية التي جمعتها : {daily_count}
• [💲] عدد النقاط اللي جمعتها من الهدايا اليومية : {all_gift}
• [🧬] عدد الطلبات التي طلبتها : {buys}
• [🛩] عدد التحويلات التي قمت بها : {trans}

{y}'''
        bot.edit_message_text(text=textt,chat_id=cid,message_id=mid,reply_markup=bk)
        return
    if data == 'setforce':
        x = bot.edit_message_text(text='• قم بارسال معرفات القنوات هكذا \n @first @second',reply_markup=bk,chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, setfo)
    if data == 'admins':
        get_admins = db.get('admins')
        if get_admins:
            if len(get_admins) >=1:
                txt = 'الادمنية : \n'
                for ran, admin in enumerate(get_admins, 1):
                    try:
                        info = bot.get_chat(admin)
                        username = f'{ran} @'+str(info.username)+' | {admin}\n' if info.username else f'{ran} {admin} .\n'
                        txt+=username
                    except:
                        txt+=f'{ran} {admin}\n'
                bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
                return
            else:
                bot.edit_message_text(chat_id=cid, message_id=mid, text=f'لا يوجد ادمنية بالبوت')
                return
        else:
            bot.edit_message_text(chat_id=cid, message_id=mid, text='لا يوجد ادمنية بالبوت')
            return
    if data == 'votes':
        db.set(f'vote_{cid}_proccess', True)
        x = bot.edit_message_text(text='• حسنا ، ارسل الان عدد التصويتات التي تريدها',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'votes'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'votes2':
        db.set(f'vote_{cid}_proccess', True)
        x = bot.edit_message_text(text='• حسنا ، ارسل الان عدد التصويتات التي تريدها',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'votes2'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'votes3':
        db.set(f'vote_{cid}_proccess', True)
        x = bot.edit_message_text(text='• حسنا ، ارسل الان عدد التصويتات التي تريدها',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'votes3'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'buy':
        keys = mk(row_width=2)
        btn6 = btn('تبديل نقاط المليار ⇌ 𝐒𝐓𝐀𝐑𝐒 ',callback_data='change_point')
        keys.add(btn6)
        keys.add(btn('‹ رجوع ↻›', callback_data='back'))
        hakem = ''' • ⌁ لشراء نقاط من بوت رشق 𝐒𝐓𝐀𝐑𝐒 💎 ⭐️↫ ⤈ :💰


⌁︰1$   ↬ 4000 IQD في البوت
⌁︰5$ ↬ 22000 IQD في البوت 
⌁︰10$ ↬ 45000 IQD في البوت
⌁︰25$ ↬ 1000000 IQD في البوت 
- - - - - - - - - - - - - - -
⌁ لتبديل نقاط من بوت رشق 𝐒𝐓𝐀𝐑𝐒 💎ة بدل المليار ↫⤈
• 3000نقطه (مليار) = 3000 نقطه
• 10000نقطه (مليار) = 12000 نقطه
•15000نقطه (مليار) = 18000 نقطه
•20000نقطه (مليار) = 25000 نقطه
• ⋯ • ⋯ • ⋯ • ⋯ • ⋯ •• ⋯ • ⋯ • ⋯ • ⋯ • 
.           ⌁ لتبديل نقاط من بوت رشق 𝐒𝐓𝐀𝐑𝐒 💎ة بدل دعمكم ↫⤈
• 3000نقطه (دعمكم) = 3000 نقطه
• 10000نقطه (دعمكم) = 12000 نقطه
•15000نقطه (دعمكم) = 18000 نقطه
•20000نقطه (دعمكم) = 25000 نقطه
• ⋯ • ⋯ • ⋯ • ⋯ • ⋯ •• ⋯ • ⋯ • ⋯ • ⋯ • 
⌁ للتواصل 
⌁︰@i_n_ub
⌁︰ يوزر البوت @ejabot  
- - - - - - - - - - - - - - -
⌁︙طرق الدفع 
⌁︰كريمي  , بايير  , آسيا , زين كاش ,نقاط دعمك
⌁︰نقاط المليار , نقاط بوت اليمن  .
ملاحظه:إذا تم كشف اي عمليه شراء من غير حسابنا الرسمي سيتم تصفير جميع نقاط الطرفين ولن يتم تعويض اي طرف⚙️ '''
        bot.edit_message_text(text=hakem,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'dump_votes':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
                return 
            db.set(f'dump_votes_{cid}_proccess', True)
            x = bot.edit_message_text(text='• حسنا ، ارسل الان رابط المنشور الذي تريد سحب المنشورات منه ',reply_markup=bk,chat_id=cid,message_id=mid)
            bot.register_next_step_handler(x, dump_votes)
        else:
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'share_link':
        bot_user = None
        try:
            x = bot.get_me()
            bot_user = x.username
        except:
            bot.edit_message_text(text=f'• حدث خطا ما في البوت',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        link = f'https://t.me/{bot_user}?start={cid}'
        y = trend()
        keys = mk(row_width=2)
        keys.add(btn('جوائز مشاركات رابط دعوة', callback_data='_givt'))
        keys.add(btn('‹ رجوع ↻›', callback_data='collect'))
        xyz = f'''
<strong>
انسخ الرابط ثم قم بمشاركته مع اصدقائك !!
</strong>
~  كل شخص يقوم بالدخول ستحصل على <strong>{link_price}</strong> نقطه

~ بإمكانك عمل اعلان خاص برابط الدعوة الخاص بك 

🌀 رابط الدعوة : \n<strong>{link}</strong> .

~ مشاركتك للرابط : <strong>{len(get(cid)["users"])} </strong>.

{y}
        '''
        bot.edit_message_text(text=xyz,chat_id=cid,message_id=mid,reply_markup=keys,parse_mode='HTML')
        return
    if data == 'members':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
                return 
            db.set(f'member_{cid}_proccess', True)
            x = bot.edit_message_text(text='• حسنا ، ارسل عدد الاعضاء التي تريد ارسالها ',reply_markup=bk,chat_id=cid,message_id=mid)
            type = 'members'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'membersp':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
                return 
            db.set(f'memberp_{cid}_proccess', True)
            x = bot.edit_message_text(text='• حسنا ، ارسل عدد الاعضاء التي تريد ارسالها ',reply_markup=bk,chat_id=cid,message_id=mid)
            type = 'membersp'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'spams':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
                return 
            db.set(f'spam_{cid}_proccess', True)
            x = bot.edit_message_text(text='• ارسل الان عدد الرسائل التي تريد ارسالها اسبام',reply_markup=bk,chat_id=cid,message_id=mid)
            type = 'msgs'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
        
    if data == 'react':
        db.set(f'react_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد التفاعلات التي تريد رشقها',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'react'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'reacts':
        db.set(f'reacts_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد التفاعلات التي تريد رشقها بشكل عشوائي',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'reactsrandom'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'forward':
        db.set(f'forward_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد التوجيهات التي تريد رشقها علي منشور القناة ',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'forward'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'view_stories':
        # bot.answer_callback_query(call.id, 'الخدمة تحت الصيانة . ', show_alert=True)
        # return
        db.set(f'view_stories_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد المشاهدات اللي تريد ترشقها ',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'view_stories'
        bot.register_next_step_handler(x, get_amount, type)

    if data == 'rect_stories':
        keys = mk(row_width=2)
        for ii in REACTIONS_LIST:
            keys.add(btn(''.join(REACTIONS_LIST[ii]), callback_data=f'rectstories|{ii}'))
        keys.add(btn('‹ رجوع ↻›', callback_data='free'))
        bot.edit_message_text(text='• اختر نوع التفاعلات',chat_id=cid,message_id=mid,reply_markup=keys)

    if data.split('|')[0] == 'rectstories':
        rect_id = data.split('|')[1]
        db.set(f'rect_stories_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد التفاعلات اللي تريد ترشقها ',reply_markup=bk,chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, get_amount_rect_Stores, rect_id)
    if data == 'click_force':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('رجوع', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='• عذرا عليك شراء عضوية VIP',chat_id=cid,message_id=mid,reply_markup=keys)
                
                return 
            x = bot.edit_message_text(text=f'• حسنا ، ارسل رابط المنشور الذي تريد التصويت عليه',chat_id=cid,message_id=mid,reply_markup=keys)
            bot.register_next_step_handler(x, get_url_click_force)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية VIP',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'view':
        db.set(f'view_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد المشاهدات اللي تريد ترشقها علي منشور القناة',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'view'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'view_2':
        db.set(f'view_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد المشاهدات اللي تريد ترشقها علي منشور القناة',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'view_2'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'poll':
        db.set(f'poll_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد الاستفتاء الذي تريد رشقه',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'poll'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'poll2':
        db.set(f'poll_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد الاستفتاء الذي تريد رشقه',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'poll2'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'userbot':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
                return 
            db.set(f'userbot_{cid}_proccess', True)
            x = bot.edit_message_text(text='• ارسل الان عدد المستخدمين الذي تريد ترشقهم للبوت الخاص بك',reply_markup=bk,chat_id=cid,message_id=mid)
            type = 'userbot'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'linkbot':
        db.set(f'linkbot_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد روابط الدعوة التي تريد رشقها',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'linkbot'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'comments':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
                return 
            db.set(f'comments_{cid}_proccess', True)
            x = bot.edit_message_text(text='• ارسل الان عدد التعليقات التي تريد رشقها ',reply_markup=bk,chat_id=cid,message_id=mid)
            type = 'comments'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'tape':
        how = ""
        x = giiiift(cid)
        if x is not None:
            duration = datetime.timedelta(seconds=x)
            noww = datetime.datetime.now()
            target_datetime = noww + duration
            remaining_time = target_datetime - noww
            hours = remaining_time.seconds // 3600
            minutes = (remaining_time.seconds % 3600) // 60
            seconds = remaining_time.seconds % 60
            if hours > 0:
                how = f"❌"
                hoow = "0/1"
            elif minutes > 0:
                how = f"❌"
                hoow = "0/1"
            else:
                how = f"❌"
                hoow = "0/1"
        else:
            how = "✅"
            hoow = "1/1"
        typ = float(db.get(f"typ_{cid}")) if db.exists(f"typ_{cid}") else 0.0
        if typ >= 100.0:
            db.set(f"typ_{cid}", 100)
            type = "██████████ ׀<"
        elif typ >= 85.0:
            type = "░▓████████ ׀<"
        elif typ >= 75.0:
            type = "░░▓███████ ׀<"
        elif typ >= 50.0:
            type = "░░░░▓█████ ׀<"
        elif typ >= 25.0:
            type = "░░░░░░▓███ ׀<"
        elif typ >= 15.0:
            type = "░░░░░░░▓██ ׀<"
        elif typ >= 0.0:
            type = "░░░░░░░░░▓ ׀<"
        if typ == 0.0:
            type = "░░░░░░░░░░ ׀<"
        keys = mk(
             [
                 [btn(text=f'الزيادة', callback_data=f'tt'),btn(text=f'الحصول', callback_data=f'tt'),btn(text=f'المتاح', callback_data=f'tt'),btn(text=f'المهام', callback_data=f'tt')],
                 [btn(text=f'0.2%', callback_data=f'tjkt'),btn(text=f'{how}', callback_data='ee'), btn(text=f'{hoow}', callback_data='kk'),btn(text=f'الهدية 🎁', callback_data=f'dailygift')],
                 [btn(text=f'0.3%', callback_data=f'tjklot'),btn(text=f'✅', callback_data='eoke'), btn(text=f'♾', callback_data='kiskk'),btn(text=f'الدعوة 🌀', callback_data=f'share_link')],
                 [btn(text=f'0.1%', callback_data=f'tjklot'),btn(text=f'✅', callback_data='eoe'), btn(text=f'♾', callback_data='kis'),btn(text=f'الانضمام 📣', callback_data=f'join_ch')],
                 [btn(text=f'0.2%', callback_data=f'tvjklot'),btn(text=f'✅', callback_data='eloe'), btn(text=f'♾', callback_data='kiskv'),btn(text=f'التمويل 📮', callback_data=f'tmoo')],
                 [btn(text=f'0.1%', callback_data=f'tvjot'),btn(text=f'✅', callback_data='elo'), btn(text=f'♾', callback_data='kkv'),btn(text=f'التحويل ♻️', callback_data=f'send')],
                 [btn(text=f'متجر المهام 🛒', callback_data='market')],
                 [btn(text=f'%{typ} ׀ {type}', callback_data='tto')],
                 [btn(text='‹ رجوع ↻›', callback_data='back')]
             ]
        )
        bot.edit_message_text(text='• مرحبا بك في قسم شريط المهام 〽️\n\n• اكمل المهام واستبدل نسبة الشريط بالهدايا والمكافات في متجر المهام ',chat_id=cid,message_id=mid,reply_markup=keys)
    typ = float(db.get(f"typ_{cid}")) if db.exists(f"typ_{cid}") else 0.0
    if typ >= 100.0:
        db.set(f"typ_{cid}", 100)
        type = "██████████ ׀<"
    elif typ >= 85.0:
        type = "░▓████████ ׀<"
    elif typ >= 75.0:
        type = "░░▓███████ ׀<"
    elif typ >= 50.0:
        type = "░░░░▓█████ ׀<"
    elif typ >= 25.0:
        type = "░░░░░░▓███ ׀<"
    elif typ >= 15.0:
        type = "░░░░░░░▓██ ׀<"
    elif typ >= 0.0:
        type = "░░░░░░░░░▓ ׀<"
    if typ == 0.0:
        type = "░░░░░░░░░░ ׀<"
    if data == 'market':
        typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
        key = mk(
            [
                [btn(text='الاتاحة', callback_data='pp'),btn(text=f'السعر', callback_data='pp'),btn(text=f'المكافأة', callback_data='pp')],
                [btn(text='قسم النقاط', callback_data='ppo')],
                [btn(text='✅', callback_data='chda'),btn(text=f'50.0%', callback_data='chda'),btn(text=f'5000 نقطة', callback_data='chda')],
                [btn(text='✅', callback_data='chd1'),btn(text=f'10.0%', callback_data='chd1'),btn(text=f'1000 نقطة', callback_data='chd1')],
                [btn(text='قسم الـ ᴠɪᴘ', callback_data='plp')],
                [btn(text='❌', callback_data='chvi'),btn(text=f'100.0%', callback_data='chvi'),btn(text=f'10 يوم ᴠɪᴘ', callback_data='chvi')],
                [btn(text='✅', callback_data='ch5'),btn(text=f'50.0%', callback_data='ch5'),btn(text=f'5 يوم ᴠɪᴘ', callback_data='ch5')],
                [btn(text='✅', callback_data='ch1'),btn(text=f'10.0%', callback_data='ch1'),btn(text=f'1 يوم ᴠɪᴘ', callback_data='ch1')],
                [btn(text=f'%{typ} ׀ {type}', callback_data='tto')],
                [btn(text='‹ رجوع ↻›', callback_data='tape')]
            ]
        )
        bot.edit_message_text(text='• مرحبا بك في متجر شريط المهام 〽️\n• يمكنك استبدال المكافات مقابل نسبة الشريط الحالية لحسابك',chat_id=cid,message_id=mid,reply_markup=key)
    if data == 'chda':
        user_id = call.from_user.id
        typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
        if typ >= 50.0:
            rk = "تهانينا ، لقد حصلت علي 5000 نقطة وتم خصم 50.0% من نسبة الشريط 🎉"
            typ = float(db.get(f"typ_{cid}")) if db.exists(f"typ_{cid}") else 0.0
            ftt = typ - 50.0
            db.set(f"typ_{cid}", float(ftt))
            info = db.get(f'user_{cid}')
            info['coins'] = int(info['coins']) + 5000
            db.set(f"user_{cid}", info)
            bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=bk)
        else:
            bot.answer_callback_query(call.id, text=f"• عذرا ، نسبة الشريط الحالية {typ} لا تكفي ❌")
    if data == 'chd1':
        user_id = call.from_user.id
        typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
        if typ >= 10.0:
            rk = "تهانينا ، لقد حصلت علي 1000 نقطة وتم خصم 10.0% من نسبة الشريط 🎉"
            typ = float(db.get(f"typ_{cid}")) if db.exists(f"typ_{cid}") else 0.0
            ftt = typ - 10.0
            db.set(f"typ_{cid}", float(ftt))
            info = db.get(f'user_{cid}')
            info['coins'] = int(info['coins']) + 1000
            db.set(f"user_{cid}", info)
            bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=bk)
        else:
            bot.answer_callback_query(call.id, text=f"• عذرا ، نسبة الشريط الحالية {typ} لا تكفي ❌")
    if data == 'dellink':
        count_coins = db.get("user_trans")
        if count_coins != 0:
            try:
                rand = db.get("user_tran")
                user_from = db.get("user_iddd")
                joo = db.get(f"user_{user_from}")
                info = db.get(f"user_{cid}")
                coins = info['coins']
                rk = f"""*• 📎] تم تعطيل الرابط , وسترداد {count_coins} نقطة ♻️*"""
                bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,parse_mode="Markdown",reply_markup=bk)
                info['coins'] = int(info['coins']) + int(count_coins)
                db.set(f"user_{cid}", info)
                db.delete('user_tran')
                db.delete('user_iddd')
            except:
                rk = f"""*• 📎] تمت انتهاء صلاحية هذا الرابط ❌*"""
                bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,parse_mode="Markdown",reply_markup=bk)
        else:
            rk = f"""*• 📎] تمت انتهاء صلاحية هذا الرابط ❌*"""
            bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,parse_mode="Markdown",reply_markup=bk)
    if data == 'chvi':
        user_id = call.from_user.id
        typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
        if typ >= 100.0:
            rk = "<strong>• تهانينا ، لقد حصلت علي 10 يوم ᴠɪᴘ  وتم خصم 100.0% من نسبة الشريط 🎉</strong>"
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
            ftt = typ - 100.0
            db.set(f"typ_{user_id}", float(ftt))
            info = db.get(f'user_{user_id}')
            info['premium'] = True
            db.set(f"user_{user_id}", info)
            users = {}
            noww = time.time()
            users['vip'] = noww
            db.set(f'vip_{user_id}', users)
            db.set(f"vipp_{user_id}_time", 5)
            us = bot.get_chat(user_id)
            if us.username is None:
                user = "لا يوجد"
            else:
                user = "@" + us.username
            name = us.first_name
            today = datetime.date.today()
            end_date = today + datetime.timedelta(days=int(10))
            now = datetime.datetime.now()
            HM = now.strftime("%p")
            if str(HM) == str("PM"):
                how = "مساءً"
            else:
                how = "صباحاً"
            hour = now.hour
            minutes = now.minute
            seconds = now.second
            d = 10
            h = 10 * 24
            m = 10 * 24 * 60
            s = 10 * 24 * 60 * 60
            reb2 = f"""*• تهانينا ، تم تفعيل ᴠɪᴘ لحسابك في البوت ✅*\n\n_• مدة الاشتراك  ⏱️:_\n\n- المدة بالايام : {d}\n- المدة بالساعات : {h}\n- المدة بالدقائق : {m}\n- المدة بالثواني : {s}\n\n*• وقت انتهاء اشتراكك :*\n\n- يوم : {end_date}\n- الساعة : {hour} {how}\n- الدقيقة : {minutes}"""
            reb = f"""*• تمت عملية تفعيل ᴠɪᴘ جديده 🔥*
`{user_id}`
*• معلومات الاشتراك والمدة ⏱:*

_• وقت التفعيل :_

- اليوم : {today}
- الساعة : {hour} {how}
- الدقيقة : {minutes}

_• مدة الاشتراك  :_

- المدة بالايام : {d}
- المدة بالساعات : {h}
- المدة بالدقائق : {m}
- المدة بالثواني : {s}

*• وقت انتهاء الاشتراك :*

_• سينتهي اشتراك العضو في :_

- يوم : {end_date}
- الساعة : {hour} {how}
- الدقيقة : {minutes}"""
            bot.send_message(chat_id=int(sudo), text=reb, parse_mode="Markdown")
            bot.send_message(chat_id=int(user_id), text=reb2, parse_mode="Markdown")
            bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=bk)
        else:
            bot.answer_callback_query(call.id, text=f"• عذرا ، هذا العرض غير متاح حالياً ❌")
    if data == 'ch5':
        user_id = call.from_user.id
        typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
        if typ >= 50.0:
            rk = "<strong>• تهانينا ، لقد حصلت علي 5 يوم ᴠɪᴘ  وتم خصم 50.0% من نسبة الشريط 🎉</strong>"
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
            ftt = typ - 50.0
            db.set(f"typ_{user_id}", float(ftt))
            info = db.get(f'user_{user_id}')
            info['premium'] = True
            db.set(f"user_{user_id}", info)
            users = {}
            noww = time.time()
            users['vip'] = noww
            db.set(f'vip_{user_id}', users)
            db.set(f"vipp_{user_id}_time", 3)
            us = bot.get_chat(user_id)
            if us.username is None:
                user = "لا يوجد"
            else:
                user = "@" + us.username
            name = us.first_name
            today = datetime.date.today()
            end_date = today + datetime.timedelta(days=int(5))
            now = datetime.datetime.now()
            HM = now.strftime("%p")
            if str(HM) == str("PM"):
                how = "مساءً"
            else:
                how = "صباحاً"
            hour = now.hour
            minutes = now.minute
            seconds = now.second
            d = 5
            h = 5 * 24
            m = 5 * 24 * 60
            s = 5 * 24 * 60 * 60
            reb2 = f"""*• تهانينا ، تم تفعيل ᴠɪᴘ لحسابك في البوت ✅*\n\n_• مدة الاشتراك  ⏱️:_\n\n- المدة بالايام : {d}\n- المدة بالساعات : {h}\n- المدة بالدقائق : {m}\n- المدة بالثواني : {s}\n\n*• وقت انتهاء اشتراكك :*\n\n- يوم : {end_date}\n- الساعة : {hour} {how}\n- الدقيقة : {minutes}"""
            reb = f"""*• تمت عملية تفعيل ᴠɪᴘ جديده 🔥*
`{user_id}`
*• معلومات الاشتراك والمدة ⏱:*

_• وقت التفعيل :_

- اليوم : {today}
- الساعة : {hour} {how}
- الدقيقة : {minutes}

_• مدة الاشتراك  :_

- المدة بالايام : {d}
- المدة بالساعات : {h}
- المدة بالدقائق : {m}
- المدة بالثواني : {s}

*• وقت انتهاء الاشتراك :*

_• سينتهي اشتراك العضو في :_

- يوم : {end_date}
- الساعة : {hour} {how}
- الدقيقة : {minutes}"""
            bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=bk)
            bot.send_message(chat_id=int(sudo), text=reb, parse_mode="Markdown")
            bot.send_message(chat_id=int(user_id), text=reb2, parse_mode="Markdown")
        else:
            bot.answer_callback_query(call.id, text=f"• عذرا ، نسبة الشريط الحالية {typ} لا تكفي ❌")
    if data == 'ch1':
        user_id = call.from_user.id
        typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
        if typ >= 10.0:
            rk = "<strong>• تهانينا ، لقد حصلت علي 1 يوم ᴠɪᴘ  وتم خصم 10.0% من نسبة الشريط 🎉</strong>"
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
            ftt = typ - 10.0
            db.set(f"typ_{user_id}", float(ftt))
            info = db.get(f'user_{user_id}')
            info['premium'] = True
            db.set(f"user_{user_id}", info)
            users = {}
            noww = time.time()
            users['vip'] = noww
            db.set(f'vip_{user_id}', users)
            db.set(f"vipp_{user_id}_time", 1)
            us = bot.get_chat(user_id)
            if us.username is None:
                user = "لا يوجد"
            else:
                user = "@" + us.username
            name = us.first_name
            today = datetime.date.today()
            end_date = today + datetime.timedelta(days=int(1))
            now = datetime.datetime.now()
            HM = now.strftime("%p")
            if str(HM) == str("PM"):
                how = "مساءً"
            else:
                how = "صباحاً"
            hour = now.hour
            minutes = now.minute
            seconds = now.second
            d = 1
            h = 1 * 24
            m = 1 * 24 * 60
            s = 1 * 24 * 60 * 60
            reb2 = f"""*• تهانينا ، تم تفعيل ᴠɪᴘ لحسابك في البوت ✅*\n\n_• مدة الاشتراك  ⏱️:_\n\n- المدة بالايام : {d}\n- المدة بالساعات : {h}\n- المدة بالدقائق : {m}\n- المدة بالثواني : {s}\n\n*• وقت انتهاء اشتراكك :*\n\n- يوم : {end_date}\n- الساعة : {hour} {how}\n- الدقيقة : {minutes}"""
            reb = f"""*• تمت عملية تفعيل ᴠɪᴘ جديده 🔥*
`{user_id}`
*• معلومات الاشتراك والمدة ⏱:*

_• وقت التفعيل :_

- اليوم : {today}
- الساعة : {hour} {how}
- الدقيقة : {minutes}

_• مدة الاشتراك  :_

- المدة بالايام : {d}
- المدة بالساعات : {h}
- المدة بالدقائق : {m}
- المدة بالثواني : {s}

*• وقت انتهاء الاشتراك :*

_• سينتهي اشتراك العضو في :_

- يوم : {end_date}
- الساعة : {hour} {how}
- الدقيقة : {minutes}"""
            bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=bk)
            bot.send_message(chat_id=int(sudo), text=reb, parse_mode="Markdown")
            bot.send_message(chat_id=int(user_id), text=reb2, parse_mode="Markdown")
        else:
            bot.answer_callback_query(call.id, text=f"• عذرا ، نسبة الشريط الحالية {typ} لا تكفي ❌")
    if data == 'lvallc':
        bot.edit_message_text(text='• تم بدء مغادرة كل القنوات والمجموعات بنجاح ✅',chat_id=cid,message_id=mid)
        acc = db.get('accounts')
        amount = len(acc)
        true = 0
        for amount in acc:
            try:
                true+=1
                o = asyncio.run(leave_chats(amount['s']))  
            except Exception as e:
                print(e)
                continue
            id = call.from_user.id
            bot.send_message(chat_id=id, text=f'• تم بنجاح الخروج من كل القنوات والمجموعات \n• تم الخروج من <code>{true}</code> حساب بنجاح ✅')
    if data == 'cancel':
        bot.edit_message_text(text='<strong>• تم الغاء عملية المغادرة ❌</strong>',chat_id=cid,message_id=mid)
    
    
    if data == 'linkbot2':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
                return
            db.set(f'linkbot2_{cid}_proccess', True)
            x = bot.edit_message_text(text='• ارسل الان عدد رشق روابط الدعوة التي تريدها',reply_markup=bk,chat_id=cid,message_id=mid)
            type = 'linkbot2'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('‹ رجوع ↻›', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᵛ͢ᵎᵖ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    else:
        return
def skip(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    user_id = call.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
    chats_dd = db.get('force_ch')
    joo = db.get(f"user_{user_id}")
    coin = joo['coins']
    chats_user = [chat for chat in chats_dd if chat not in chats_joining]
    doo = db.get('force_ch')
    if doo != None:
        for i in chats_user:
            chats_joining.append(i)
            db.set(f"chats_{user_id}", chats_joining)
            nextch(call)
            return
def nextch(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    user_id = call.from_user.id
    v = 5
    if v == 5:
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        doo = db.get('force_ch')
        threading.Thread(target=CeckAnjoens,args=(user_id,)).start()
        if doo != None:
            for i in chats_user:
                count = db.get(f"count_{i}")
                ids = db.get(f"id_{i}")
                Status = requests.get(f"https://api.telegram.org/bot{token_helper}/getChatMember?chat_id={i}&user_id={ids}").json()["ok"]
                if Status:
                    
                    if int(count) <= 2:
                        
                        tm = db.get("tmoil") if db.exists("tmoil") else 0
                        tmm = int(tm) + 1
                        db.set("tmoil", int(tmm))
                        chats_dd = db.get('force_ch')
                        chats_dd.remove(i)
                        db.set("force_ch", chats_dd)
                        chat_info = bot.get_chat(i)
                        name = chat_info.title
                        ii = i.replace('@', '')
                        mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else "عدد غير معروف"
                        bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك @{ii} ب {mem} عضو 🚸", parse_mode="Markdown")
                        iddd = 6360165330
                        bot.send_message(chat_id=int(iddd), text=f"*تم انتهاء تمويل قناتك *[{name}](https://t.me/{ii})* بنجاح ✅*\n*• تم تمويل : {mem} عضو* 🚸", parse_mode="Markdown")
                    else: 
                        chat_info = bot.get_chat(i)
                        name = chat_info.title
                        ii = i.replace('@', '')
                        k = f'''• اشترك في القناة : {i} 📣'''
                        keys = mk(
                            [
                                [btn(text=f'{name}', url=f'https://t.me/{ii}')],
                                [btn(text='اشتركت ✅', callback_data='check_join'), btn(text='تخطي 🚸', callback_data='skip')],
                                [btn(text='‹ رجوع ↻›', callback_data='collect')]
                            ]
                        )
                        bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys)
                        return
            kk = f"• لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه ❕\n• اذا قمت بمغادرة اي قناة سيتم خصم ضعف النقاط"
            key = mk(
                [
                    [btn(text='تجميع النقاط ', callback_data='collect')],
                    [btn(text='الغاء ❌', callback_data='back')]
                ]
            )
            bot.edit_message_text(text=kk, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
def tmmo(msg):
    user_id = msg.from_user.id
    if not db.get(f'tmoo_{msg.from_user.id}_proccess'): return
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
    joo = db.get(f"user_{user_id}")
    price_join = db.get("price_join") if db.exists("price_join") else 10
    coin = int(joo['coins'])
    try:
        count = int(msg.text)
    except:
        bot.reply_to(msg, '• يجب ان يكون عدد فقط ❌')
        return
    if count <15:
        bot.reply_to(msg, "اقل حد للطلب هو 15 ❌")
        return
    all = int(price_join) * int(count)
    joo = db.get(f"user_{user_id}")
    if joo['coins'] < int(all):
        bot.reply_to(msg, "• عفوا ، نقاطك لا تكفي لهذا الطلب ❌")
        return
    x = bot.reply_to(msg, "• ارفع البوت المساعد @hdrtyrdbot ادمن في قناتك او مجموعتك\n\n• ثم ارسل المعرف او الرابط الخاص بالقناة او المجموعة 👥")
    bot.register_next_step_handler(x, tmm_count, count)
def tmm_count(msg,count):
    user_id = msg.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
    joo = db.get(f"user_{user_id}")
    price_join = db.get("price_join") if db.exists("price_join") else 10
    channel = msg.text.replace('https://t.me/', '@').replace('@', '@')
    channels_force = db.get("force_ch") if db.exists("force_ch") else []
    channel_username = channel.lower().strip()
    balcklist = db.get('chat_blacklist')
    if channel_username in balcklist:
        bot.send_message(text='عذرن تم حضر قناتك من البوت بي شكل نهائي . ', chat_id=msg.chat.id)
        return 
    try:
        chat_member = bot2.get_chat_member(channel_username, bot2.get_me().id)
    except:
        bot.reply_to(msg, "* لا يوجد قناة او مجموعة تحمل هذا المعرف ❌*", parse_mode="Markdown")
        return False
    if str(chat_member.status) == "administrator":
        if channel_username in channels_force:
            count_befor = db.get(f"count_{channel_username}")
            alll = int(count_befor) + int(count)
            all_coins = int(price_join) * int(count)
            joo = db.get(f"user_{user_id}")
            joo['coins'] = int(joo['coins']) - int(all_coins)
            db.set(f"user_{user_id}", joo)
            db.set(f"count_{channel_username}", alll)
            db.set(f"mem_{channel_username}", alll)
            db.set(f"id_{channel_username}", user_id)
            chat_info = bot.get_chat(channel_username)
            name = chat_info.title
            ii = channel_username.replace('@', '')
            all_coins = int(price_join) * int(count)
            bot.reply_to(msg, f"• تم خصم ({all_coins}) نقاط\n- وبدء تمويل قناتك [{name}](https://t.me/{ii}) بـ {alll} عضو 🚸\n• تاكد من عدم ازالة البوت من الادمنية حتي لا يتم استبعاد تمويلك", parse_mode="Markdown")
            bot.send_message(chat_id=int(sudo), text=f"- بدء تمويل قناة جديدة [{name}](https://t.me/{ii}) بـ {alll} عضو 🚸", parse_mode="Markdown")
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
            ftt = typ + 0.2
            db.set(f"typ_{user_id}", float(ftt))
            my_tmm = db.get(f"my_tmm_{user_id}") if db.exists(f"my_tmm_{user_id}") else []
            if channel_username not in my_tmm:
                my_tmm.append(channel_username)
                db.set(f"my_tmm_{user_id}", my_tmm)
        else:
            all = int(price_join) * int(count)
            joo = db.get(f"user_{user_id}")
            joo['coins'] = int(joo['coins']) - int(all)
            db.set(f"user_{user_id}", joo)
            db.set(f"count_{channel_username}", count)
            db.set(f"mem_{channel_username}", count)
            db.set(f"id_{channel_username}", user_id)
            channels_force = db.get("force_ch") if db.exists("force_ch") else []
            channels_force.append(channel_username)
            db.set("force_ch", channels_force)
            chat_info = bot.get_chat(channel_username)
            name = chat_info.title
            ii = channel_username.replace('@', '')
            bot.reply_to(msg, f"• تم خصم ({all}) نقاط\n- وبدء تمويل قناتك [{name}](https://t.me/{ii}) بـ {count} عضو 🚸\n\n• تاكد من عدم ازالة البوت من الادمنية حتي لا يتم استبعاد تمويلك", parse_mode="Markdown")
            bot.send_message(chat_id=int(sudo), text=f"- بدء تمويل قناة جديدة [{name}](https://t.me/{ii}) بـ {count} عضو 🚸", parse_mode="Markdown")
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
            ftt = typ + 0.2
            db.set(f"typ_{user_id}", float(ftt))
            my_tmm = db.get(f"my_tmm_{user_id}") if db.exists(f"my_tmm_{user_id}") else []
            if channel_username not in my_tmm:
                my_tmm.append(channel_username)
                db.set(f"my_tmm_{user_id}", my_tmm)
    else:
        bot.reply_to(msg, "*البوت غير مشرف بهذه القناة ❌*", parse_mode="Markdown")
        return
        
def get_amount_rect_Stores(message, rect_id):
    admins = db.get('admins')
    cid = message.from_user.id
    if not db.get(f'rect_stories_{cid}_proccess'): return
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
        return
    if amount < 1:
        bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
        return
    if amount > 200:
        bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>200</strong> ..',reply_markup=bk)
        return
    pr = rect_stories_price * amount
    acc = db.get(f'user_{message.from_user.id}')
    if int(pr) > acc['coins']:
        bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
        return
    load_ = db.get('accounts')
    if len(load_) < amount:
        bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
        return
    x = bot.reply_to(message,f'• قم بارسال رابط الاستوري الذي تريد رشفه الكمية<strong>{amount}</strong>')
    bot.register_next_step_handler(x, get_rect_stories_url, amount, rect_id)
    return

def get_amount(message, type):
    admins = db.get('admins')
    cid = message.from_user.id

    if type == 'leavs':
        if not db.get(f'leave_{cid}_proccess'): return
        if detect(message.text):
            url = message.text
            acc = db.get('accounts')
            amount = len(acc)
            if len(acc) > 10:
                amount = amount / 2
            true = 0
            for y in acc:
                true+=1
                if true >=amount:
                    break
                try:
                    o = asyncio.run(leave_chats(y['s'], url))
                    
                except Exception as e:
                    
                    continue
            bot.reply_to(message, f'• تم الخروج من <code>{true}</code> حساب ينجاح ✅')
            return
                    
        else:
            url = message.text.replace('https://t.me/', '').replace('@', '')
            acc = db.get('accounts')
            amount = len(acc)
            if len(acc) > 10:
                amount = amount / 2
            true = 0
            for y in acc:
                
                if true >=amount:
                    break
                try:
                    o = asyncio.run(leave_chat(y['s'], url))
                   
                    true+=1
                except Exception as e:
                    
                    continue
            bot.reply_to(message, f'• تم الخروج من <strong>{true}</strong> حساب ✅')
            return
            pass
    if type == 'tom_rect':
        if not db.get(f'rect_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>0</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان عدد المنشورات التي تريد رشقها بمشاهدات تلقائيا')
            bot.register_next_step_handler(x, get_amount_tom_rect, amount)
            return
    if type == 'tom_view':
        if not db.get(f'view_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>0</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان عدد المنشورات التي تريد رشقها بمشاهدات تلقائيا')
            bot.register_next_step_handler(x, get_amount_tom_view, amount)
            return
    if type == 'members':
        if not db.get(f'member_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 10:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>200</strong> ..',reply_markup=bk)
                return
            pr = member_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان معرف قناتك او رابطها')
            bot.register_next_step_handler(x, get_url_mem, amount)
            return
    if type == 'membersp':
        if not db.get(f'memberp_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 10:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong> ..',reply_markup=bk)
                return
            pr = member_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بالقناة الخاصة')
            bot.register_next_step_handler(x, get_url_memp, amount)
            return
    if type == 'positive':
        if not db.get(f'reacts_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>0</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = react_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n• ارسل الان رابط المنشور الذي تريد رشقه')
            bot.register_next_step_handler(x, get_positive_url, amount)
            return
    if type == 'story':
        if not db.get(f'reacts_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 10:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong> ..',reply_markup=bk)
                return
            pr = story_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n• ارسل الان رابط المنشور الذي تريد رشقه')
            bot.register_next_step_handler(x, get_story_url, amount)
            return
    if type == 'negative':
        if not db.get(f'reacts_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>0</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = react_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n• ارسل الان رابط المنشور الذي تريد رشقه')
            bot.register_next_step_handler(x, get_negative_url, amount)
            return
    if type == 'react':
        if not db.get(f'react_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong> ..',reply_markup=bk)
                return
            pr = react_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان التفاعل الذي تريد ارساله')
            bot.register_next_step_handler(x, get_react, amount)
            return
    if type == 'force_vote':
        if not db.get(f'vote_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>0</strong>',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>2000</strong>',reply_markup=bk)
                return
            pr = vote_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'نقاطك غير كافية لتنفيذ طلبك ، تحتاج الى {pr-amount} نقطة .')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : {amount} عضو\n• الان ارسل وقت الإنتضار بين الرشق (بالثواني) \n\n• ارسل 0 اذا كنت تريده فوري\n• يجب ان لايزيد عن 200')
            bot.register_next_step_handler(x, get_time_force_vote, amount)
            return
    if type == 'forward':
        if not db.get(f'forward_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong>',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong>',reply_markup=bk)
                return
            pr = forward_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور الذي تريد رشق التوجيهات عليه')
            bot.register_next_step_handler(x, get_url_forward, amount)
            return
    if type == 'poll':
        if not db.get(f'poll_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong>',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong>',reply_markup=bk)
                return
            pr = poll_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور الذي تريد رشق التوجيهات عليه')
            bot.register_next_step_handler(x, get_url_poll, amount)
            return
    if type == 'poll2':
        if not db.get(f'poll_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong>',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong>',reply_markup=bk)
                return
            pr = poll_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور الذي تريد رشق التوجيهات عليه')
            bot.register_next_step_handler(x, get_url_poll_2, amount)
            return
    if type == 'reactsrandom':
        if not db.get(f'reacts_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong> ..',reply_markup=bk)
                return
            pr = react_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• تم اختيار الكمية <strong>{amount}</strong>\n• ارسل الان رابط المنشور الذي تريد رشقه')
            bot.register_next_step_handler(x, get_reacts_url, amount)
            return
    if type == 'view_stories':
        if not db.get(f'view_stories_{cid}_proccess'): 
            return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong> ..',reply_markup=bk)
                return
            pr = view_stories_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• قم بارسال رابط الاستوري الذي تريد رشفه الكمية<strong>{amount}</strong>')
            bot.register_next_step_handler(x, get_view_stories_url, amount)
            return
    if type == 'view':
        if not db.get(f'view_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong> ..',reply_markup=bk)
                return
            pr = view_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور الذي تريد رشقه')
            bot.register_next_step_handler(x, get_view_url, amount)
            return
    if type == 'view_2':
        if not db.get(f'view_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong> ..',reply_markup=bk)
                return
            pr = view_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور الذي تريد رشقه')
            bot.register_next_step_handler(x, get_view_url_2, amount)
            return
    if type == 'votes2':
        ##print("dfdsfsdfdsf")
        if not db.get(f'vote_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>10</strong>',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>1000</strong>',reply_markup=bk)
                return
            pr = vote_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'نقاطك غير كافية لتنفيذ طلبك ، تحتاج الى {pr-amount} نقطة .')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• تم اختيار الكمية {amount} عضو\n• الان ارسل وقت الإنتضار بين الرشق (بالثواني) \n\n• ارسل 0 اذا كنت تريده فوري\n• يجب ان لايزيد عن 200')
            bot.register_next_step_handler(x, get_time_votes_2, amount)
            return
    if type == 'votes3':
        ##print("dfdsfsdfdsf")
        if not db.get(f'vote_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>10</strong>',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>1000</strong>',reply_markup=bk)
                return
            pr = vote_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'نقاطك غير كافية لتنفيذ طلبك ، تحتاج الى {pr-amount} نقطة .')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• تم اختيار الكمية {amount} عضو\n• الان ارسل وقت الإنتضار بين الرشق (بالثواني) \n\n• ارسل 0 اذا كنت تريده فوري\n• يجب ان لايزيد عن 200')
            bot.register_next_step_handler(x, get_time_votes_3, amount)
            return
    if type == 'votes':
        if not db.get(f'vote_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>10</strong>',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>1000</strong>',reply_markup=bk)
                return
            pr = vote_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'نقاطك غير كافية لتنفيذ طلبك ، تحتاج الى {pr-amount} نقطة .')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• تم اختيار الكمية {amount} عضو\n• الان ارسل وقت الإنتضار بين الرشق (بالثواني) \n\n• ارسل 0 اذا كنت تريده فوري\n• يجب ان لايزيد عن 200')
            bot.register_next_step_handler(x, get_time_votes, amount)
            return
    
    if type == 'msgs':
        if not db.get(f'spam_{cid}_proccess'): return
        if message.text:
            amount = None
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message,f'• رجاء ارسل عدد فقط ، اعد المحاولة لاحقا',reply_markup=bk)
                return
            load_ = db.get('accounts')
            if amount < 1:
                bot.reply_to(message, f'• رجاء ارسل عدد اكبر من 10', reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'• رجاء ارسل عدد اقل من 1000',reply_markup=bk)
                return
            
            if len(load_) < amount:
                bot.reply_to(message,text=f'• عدد حسابات البوت لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            pr = spam_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if acc['coins'] < pr:
                bot.reply_to(message,f'• نقاطك غير كافية لتنفيذ طلبك ، تحتاج الى {pr-amount} نقطه',reply_markup=bk)
                return
            x = bot.reply_to(message,text=f'• الان ارسل يوزر او رابط الحساب اللي تريد تعمل سبام عليه')
            bot.register_next_step_handler(x, get_url_spam, amount)
            return
    if type == 'userbot':
        if not db.get(f'userbot_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong> ..',reply_markup=bk)
                return
            pr = userbot_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط ااو معرف البوت اللي تريد ترشقله مستخدمين')
            bot.register_next_step_handler(x, get_bot_user, amount)
            return
    if type == 'linkbot':
        if not db.get(f'linkbot_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong> ..',reply_markup=bk)
                return
            pr = linkbot_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بك ')
            bot.register_next_step_handler(x, link_bot, amount)
            return
    if type == 'linkbot2':
        if not db.get(f'linkbot2_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong> ..',reply_markup=bk)
                return
            pr = linkbot2_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بك ')
            bot.register_next_step_handler(x, link_bot2, amount)
            return
    if type == 'comments':
        if not db.get(f'comments_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 1000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>1000</strong> ..',reply_markup=bk)
                return
            pr = comment_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور اللي تريد التعليق عليه \n\n يجب ان تنسخ منشور القناة من مجموعة المناقشة وليس من القناة نفسها')
            bot.register_next_step_handler(x, get_comments_url, amount)
            return
###########

def get_time_votes(message, amount):
    try:
        time = int(message.text)
    except:
        x = bot.reply_to(message,text=f'• رجاء ارسل الوقت بشكل صحيح')
        return
    if time <0:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    if time >200:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    x = bot.reply_to(message,f'• الكمية {amount}\n• الوقت بين التصويت : {time}\n\n• الان أرسل لي رابط المنشور')
    bot.register_next_step_handler(x, get_url_votes, amount, time)


def get_time_votes_2(message, amount):
    try:
        time = int(message.text)
    except:
        x = bot.reply_to(message,text=f'• رجاء ارسل الوقت بشكل صحيح')
        return
    if time <0:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    if time >200:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    x = bot.reply_to(message,f'• الكمية {amount}\n• الوقت بين التصويت : {time}\n\n• الان أرسل لي رابط المنشور')
    bot.register_next_step_handler(x, get_url_votes_2, amount, time)



def get_time_votes_3(message, amount):
    try:
        time = int(message.text)
    except:
        x = bot.reply_to(message,text=f'• رجاء ارسل الوقت بشكل صحيح')
        return
    if time <0:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    if time >200:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    x = bot.reply_to(message,f'• الكمية {amount}\n• الوقت بين التصويت : {time}\n\n• الان أرسل لي رابط المنشور')
    bot.register_next_step_handler(x, get_url_votes_3, amount, time)

def link_bot2(message, amount):
    url = message.text
    if 'https://t.me' in url:
        x = bot.reply_to(message,text=f'• الكمية : {amount}\n• الرابط : {url}\n\n• الان ارسل رابط او معرف قناة الاشتراك الاجبارى')
        bot.register_next_step_handler(x, linkbot_chforce, amount, url)
    else:
        x = bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
def dump_votes(message):

    url = message.text
    load_ = db.get('accounts')
    num = len(load_)
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'سحب تصويت'
    v = bot.reply_to(message,text=f'• تم بدء طليك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n')
    
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    for num in load_:
        try:
            x = asyncio.run(dump_votess(num['s'], url))
           
            if x == 'o':
                continue
            if x == True:
                true += 1
            else:
                false += 1
        except Exception as e:
            print(f"Erorr: {e}")
            continue
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n\n• تم سحب : {false} تصويت\n• لم يتم سحب : {true}',reply_markup=bk)
def linkbot_chforce(message, amount, url): 
    stk.Add(message.from_user.id,"yes")
    channel_force = message.text.replace('https://t.me/', '').replace('@', '')
    bot_id, user_id = url.split("?start=")[0].split("/")[-1], url.split("?start=")[1]
    channel = "@" + bot_id
    tex = "/start " + user_id
    pr = linkbot2_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'رابط دعوة اشتراك اجبارى'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : ')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    key = mk(
                [
                    
                    [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
                ]
            )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(linkbot2(y['s'], channel, tex, channel_force))
            if x == 'o':
                continue
            if x == True:
                Mens = linkbot2_price * 1
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return
##################
def get_comments_url(message, amount):
    url = message.text
    admins = db.get('admins')
    if 'https://t.me' in url:
        x = bot.reply_to(message,text=f'• الكمية : {amount}\n• الرابط : {url}\n\n• الان ارسل التعليق الذي تريد رشقه')
        bot.register_next_step_handler(x, comment_text, amount, url)
    else:
        x = bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
def comment_text(message, amount, url):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    text = message.text
    if text:
        if len(text) > 100:
            bot.reply_to(message, text='• ارسل رسالة تكون اقل من 100 حرف ')
            return
        acc = db.get(f'user_{message.from_user.id}')
        pr = comment_price * amount
        load_ = db.get('accounts')
        typerr = 'تعليقات خدمة ᵛ͢ᵎᵖ'
        v=bot.reply_to(message,text=f'• جارى تنفيذ طلبك بنجاح ✅')
        bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr} .\n• العدد : {amount}\n• الرابط : {url}\n• ايديه: {message.from_user.id} \n• يوزره : @{message.from_user.username}')
        true,Mens, false = 0,0,0      
        key = mk(
            [
                
                [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
            ]
            )
        for y in load_:
            res = stk.Get(message.from_user.id)
            if res=="no": 
                bot.send_message(message.chat.id, "تم الايقاف")
                break
            if true >= amount:
                break
            try:
                x = asyncio.run(send_comment(y['s'], url, text))
                Mens = linkbot2_price * 1
                true += 1
            except:
                false += 1
                continue
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        if true >= 1:
            acc['coins'] -= Mens
            db.set(f'user_{message.from_user.id}', acc)
        else:
            pass
        addord()
        user_id = message.from_user.id
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        buys+=1
        db.set(f"user_{user_id}_buys", int(buys))
        bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true} \n• لم يتم ارسال : {false}\n• تم خصم : {Mens} من رصيدك',reply_markup=bk)
        return
########################

def link_bot(message, amount):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    bot_id, user_id = url.split("?start=")[0].split("/")[-1], url.split("?start=")[1]
    channel = "@" + bot_id
    tex = "/start " + user_id
    pr = linkbot_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'رابط دعوة بدون اشتراك اجبارى'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ ')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0, 0,0
        
    key = mk(
    [ 
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ])
    for y in load_:    
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(linkbot(y['s'], channel, tex))
            if x == 'o':
                continue
            if x == True: 
                Mens += linkbot_price * 1
                true += 1
            else:
                ##print(linkbot_price)
                
                false += 1
            x = bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:  
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return

def get_bot_user(message, amount):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text.replace('https://t.me/', '').replace('@', '')
    pr = userbot_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'مستخدمين بوت'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ :')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(userbot(y['s'], url))
           
            if x == 'o':
                continue
            if x == True:
                Mens = userbot_price
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return
    
def get_url_spam(message, amount):
    url = message.text
    admins = db.get('admins')

    if 'https://t.me' in url or '@' in url:
        x = bot.reply_to(message,text=f'• الان ارسل الرسالة اللي تريد ترسلها للحساب')
        bot.register_next_step_handler(x, get_text, amount, url)
        return

def get_text(message, amount, url):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    text = message.text
    if text:
        if len(text) > 1000:
            bot.reply_to(message, text='• ارسل رسالة تكون اقل من 1000 حرف ')
            return
        acc = db.get(f'user_{message.from_user.id}')
        pr = spam_price * amount
        load_ = db.get('accounts')
        typerr = 'رسائل مزعجة خدمة ᵛ͢ᵎᵖ'
        v=bot.reply_to(message,text=f'• جارى تنفيذ طلبك بنجاح ✅')
        bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr} .\n• العدد : {amount}\n• الرابط : {url}\n• ايديه: {message.from_user.id} \n• يوزره : @{message.from_user.username}')
        true,Mens, false = 0,0,0
        key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
        for y in load_:
            res = stk.Get(message.from_user.id)
            if res=="no": 
                bot.send_message(message.chat.id, "تم الايقاف")
                break
            if true >= amount:
                break
            try:
                x = asyncio.run(send_message(y['s'], chat=url, text=text))
                Mens = userbot_price 
                true += 1
            except:
                false += 1
                continue
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        if true >= 1:
            
            acc['coins'] -= Mens
            db.set(f'user_{message.from_user.id}', acc)
        else:
            pass
        addord()
        user_id = message.from_user.id
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        buys+=1
        db.set(f"user_{user_id}_buys", int(buys))
        bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true} \n• لم يتم ارسال : {false}\n• تم خصم : {Mens} من رصيدك',reply_markup=bk)
        return

def get_url_memp(message, amount):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    load = db.get('accounts')
    info = get(message.from_user.id)
    price = member_price * amount
    if price > int(info['coins']):
        bot.reply_to(message,text=f'نقاطك غير كافية لتنفيذ طلبك تحتاج الى <strong> {price - int(info["coins"])} </strong>',reply_markup=bk)
        return
    if len(load) < 1:
        bot.reply_to(message,text='عدد حسابات البوت لا تكفي لتنفيذ طلبك ',reply_markup=bk)
        return
    typerr = 'رشق اعضاء قناة خاصة خدمة ᵛ͢ᵎᵖ'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت \n• النوع: {typerr}\n• العدد : {amount}\n• الرابط : {url}\n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    for y in load:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(join_chatp(y['s'], url))
            if x == 'o':
                continue
            if x == True:
                Mens += userbot_price
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            pass
    if true >= 1:
        
        info['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', info)
    else:
        pass
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true} .\n• لم يتم ارسال : {false}\n• تم خصم : {Mens} من رصيدك ',)
    db.set(f"serv_{message.from_user.id}", False)
    return

def get_url_mem(message, amount):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    if 'https://t.me' in url or '@' in url:
        if detect(url):
            load = db.get('accounts')
            info = get(message.from_user.id)
            price = member_price * amount
            if price > int(info['coins']):
                bot.reply_to(message,text=f'مامعك نقاط كافية، تحتاج <strong> {price - int(info["coins"])} </strong> نقطة علمود ترسل هذا العدد',reply_markup=bk)
                return
            if len(load) < 1:
                bot.reply_to(message,text='عدد حسابات البوت لا تكفي لتنفيذ طلبك ',reply_markup=bk)
                return
            typerr = 'رشق اعضاء خدمة ᵛ͢ᵎᵖ'
            v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅')
            db.set(f"serv_{message.from_user.id}", True)
            bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت \n• النوع: {typerr}\n• العدد : {amount}\n• الرابط : {url}\n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}')
            true,Mens, false = 0,0,0
            key = mk(
            [
                
                [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
            ]
            )
            for y in load:
                res = stk.Get(message.from_user.id)
                if res=="no": 
                    bot.send_message(message.chat.id, "تم الايقاف")
                    break
                if true >= amount:
                    break
                try:
                    x = asyncio.run(join_chat(y['s'], url))
                    if x == 'o':
                        continue
                    if x == True:
                        Mens += userbot_price
                        true += 1
                    else:
                        false += 1
                    bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
                except Exception as e:
                   pass
            if true >= 1:
                
                info['coins'] -= Mens
                db.set(f'user_{message.from_user.id}', info)
            else:
                pass
            bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true} .\n• لم يتم ارسال : {false}\n• تم خصم : {Mens} من رصيدك ',)
            db.set(f"serv_{message.from_user.id}", False)
            return
        else:
            stk.Add(message.from_user.id,"yes")
            username = url.replace('https://t.me/', '').replace('@', '')
            load = db.get('accounts')
            info = get(message.from_user.id)
            price = member_price * amount
            if price > int(info['coins']):
                bot.reply_to(message,text=f'• نقاطك غير كافية : تحتاج الى <strong> {price - int(info["coins"])} </strong> نقطة',reply_markup=bk)
                return
            if len(load) < 1:
                bot.reply_to(message,text=f'• حسابات البوت لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            typerr = 'رشق اعضاء خدمة ᵛ͢ᵎᵖ'
            v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅')
            bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount}\n• الرابط : {url}\n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
            db.set(f"serv_{message.from_user.id}", True)
            true,Mens, false = 0,0,0
            for y in load:
                res = stk.Get(message.from_user.id)
                if res=="no": 
                    bot.send_message(message.chat.id, "تم الايقاف")
                    break
                if true >= amount:
                    break
                try:
                    x = asyncio.run(join_chat(y['s'], username))
                    if x == 'o':
                        continue
                    if x == True:
                        Mens += userbot_price  
                        true += 1
                    else:
                        false += 1
                    bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
                except Exception as e:
                   
                    continue
            
            info['coins'] -= Mens
            db.set(f'user_{message.from_user.id}', info)
            addord()
            user_id = message.from_user.id
            buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
            buys+=1
            db.set(f"user_{user_id}_buys", int(buys))
            bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true} \n• لم يتم ارسال : {false}\n• تم خصم : {Mens} من رصيدك',)
            db.set(f"serv_{message.from_user.id}", False)
            return
def check_url_stories(url: str):
        pattern = r'https?://t\.me/(\w+)/(\w+)/(\d+)'
        math = re.match(pattern, url)
        if math:
                return True
        else:
                return False
def chtime(msg):
    try:
        time = int(msg.text)
    except:
        bot.reply_to(msg, text='خطا ، قم بارسال الوقت كارقام فقط ❌')
        return
    if time <0:
        bot.reply_to(msg, text='خطا ، اقل قيمة يمكن اضافتها هي 0 ❌')
        return
    if time >200:
        bot.reply_to(msg, text='خطا ، اكبر قيمة يمكن ادخالها هي 200 ❌')
        return
    db.set(f"tim_{msg.from_user.id}", int(time))
    bot.reply_to(msg, text='نجاح ، تم حفظ القيمة بنجاح ✅')
def checks(link):
    admins = db.get('admins')
    pattern = r"https?://t\.me/(\w+)/(\d+)"
    match = re.match(pattern, link)

    if match:
        username = match.group(1)
        post_id = match.group(2)
        return username, post_id
    else:
        return False

# def CHECK_USERNAME(bot: TeleBot, username : str):
#     try:
#         bot.get_chat(f'@{username}')
#         return True
#     except:
#         return False
    
def CHECK_USERNAME(username : str):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):return False
    else:return True
    
def get_react(message, amount):
    rs = ["👍","🤩","🎉","🔥","❤️","🥰","🥱","🥴","🌚","🍌","💔","🤨","😐","🖕","😈","👎","😁","😢","💩","🤮","🤔","🤯","🤬","💯","😍","🕊","🐳","🤝","👨","🦄","🎃","🤓","👀","👻","🗿","🍾","🍓","⚡️","🏆","🤡","🌭","🆒","🙈","🎅","🎄","☃️","💊"]
    if message.text in rs:
        x = bot.reply_to(message,f'• تم اختيار الكمية {amount}\n• التفاعل : {message.text}\n\n• ارسل الان رابط المنشور لرشق التفاعلات عليه')
        bot.register_next_step_handler(x, get_url_react, amount, message)
    else:
        x = bot.reply_to(message,f'• رجاء ارسل التفاعل بشكل صحيح')
        bot.register_next_step_handler(x, get_react, amount)
        return
    

def get_url_votes(message, amount, time):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = vote_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تصويت'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : ')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}\n• الوقت بين التصويت : {time} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(vote_one(y['s'], url, time))
           
            if x == 'o':
                continue
            if x == True:
                Mens += vote_price

                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لك يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return

def get_positive_url(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير الحالي ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    if "/c/" in url:
        bot.reply_to(message,text=f'• عذرا لا يمكنك استخدام الخدمة في القنوات الخاصة')
        return
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = react_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تفاعلات ايجابي [👍,❤,🔥,😍,🤩]'
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    nume = int(amount)
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ :')
    for y in load_:
        if true >= amount:
            break
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        try:
            x = asyncio.run(positive(y['s'], url))
            if x == 'o':
                continue
            if x == True:
                Mens += react_price 
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        acc = db.get(f'user_{message.from_user.id}')
        for ix in range(true):
            acc['coins'] -= react_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False) 
    addord()
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    return
def get_negative_url(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير الحالي ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    if "/c/" in url:
        bot.reply_to(message,text=f'• عذرا لا يمكنك استخدام الخدمة في القنوات الخاصة')
        return
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = react_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تفاعلات سلبي [👎,💩,🤮,🤬,🖕]'
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    nume = int(amount)
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ :')
    for y in load_:
        if true >= amount:
            break
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        try:
            x = asyncio.run(negative(y['s'], url))
           
            if x == 'o':
                continue
            if x == True:
                Mens += react_price 
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        acc = db.get(f'user_{message.from_user.id}')
        for ix in range(true):
            acc['coins'] -= react_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)


def get_url_votes_3(message, amount, time):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = vote_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تصويت'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : ')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}\n• الوقت بين التصويت : {time} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(vote_one_and_3(y['s'], url, time))
           
            if x == 'o':
                continue
            if x == True:
                Mens += vote_price

                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لك يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return

def get_url_votes_2(message, amount, time):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = vote_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تصويت'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : ')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}\n• الوقت بين التصويت : {time} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(vote_one_and_veos(y['s'], url, time))
           
            if x == 'o':
                continue
            if x == True:
                Mens += 15

                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لك يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return


  


def get_url_react(message, amount, like):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    like = like.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = react_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تفاعلات اختياري'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : ')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(reactions(y['s'], url, like))
           
            if x == 'o':
                continue
            if x == True:
                Mens += userbot_price
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لك يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return
def get_reacts_url(message, amount):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = react_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تفاعلات عشوائي'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(reaction(y['s'], url))
           
            if x == 'o':
                continue
            if x == True:
                Mens += userbot_price
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return
def get_url_forward(message, amount):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = forward_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'توجيهات'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ :')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(forward(y['s'], url))
           
            if x == 'o':
                continue
            if x == True:
                Mens += userbot_price 
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return
def get_time_force_vote(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير الحالي ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    try:
        time = int(message.text)
    except:
        x = bot.reply_to(message,text=f'• رجاء ارسل الوقت بشكل صحيح')
        return
    if time <0:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    if time >200:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    x = bot.reply_to(message,f'• الكمية : {amount}\n• الوقت بين التصويت : {time}\n\n• الان أرسل لي رابط الدعوة الخاص بالقناة الخاصة ')
    bot.register_next_step_handler(x, get_url_force_vote, amount, time)
def get_url_force_vote(message, amount, time):
    invite_link = message.text
    if "https://t.me/" not in invite_link:
        bot.reply_to(message,text=f'• رجاء ارسل رابط الدعوة بشكل صحيح')
        return
    x = bot.reply_to(message,f'• الكمية : {amount}\n• الوقت بين التصويت : {time}\n• رابط الدعوة : {invite_link}\n\n• انسخ الان رابط المنشور الذي تريد التصويت عليه ف القناة الخاصة\n• مثال : \nhttps://t.me/c/1896391380/58')
    bot.register_next_step_handler(x, get_url_force_vote_link, invite_link, amount, time)
def get_url_force_vote_link(message, invite_link, amount, time):
    url = message.text
    if "https://t.me/c/" not in url:
        bot.reply_to(message,text=f'• رجاء ارسل رابط المنشور بشكل صحيح')
        return
    msg_id = url.split("/")[-1]
    pr = vote_price * amount
    load_ = db.get('accounts')
    typerr = 'تصويتات قناة خاصة'
    db.set(f"serv_{message.from_user.id}", True)
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}\n• الوقت بين التصويت : {time} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    nume = int(amount)
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ :')
    for y in load_:
        if true >= amount:
            break
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        try:
            x = asyncio.run(force_vote(y['s'], invite_link, msg_id, time))
           
            if x == 'o':
                continue
            if x == True:
                Mens += vote_price 
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        acc = db.get(f'user_{message.from_user.id}')
        for ix in range(true):
            acc['coins'] -= vote_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    return
def get_url_poll(message, amount):
    admins = db.get('admins')
    url = message.text
    x = checks(url)
    if x:
        channel, msg_id = x
    if not checks(url):
        bot.reply_to(message,text='• رجاء ارسل الرابط بشكل صحيح')
        return
    try:
        mm = "• ارسل الان تسلسل الإجابة في الاستفتاء\n\n• يجب ان يتراوح بين 0 : 9\n• علما بان اول اختيار يكون تسلسلة 0"
        x = bot.reply_to(message, mm, parse_mode='HTML')
        bot.register_next_step_handler(x, start_poll, amount, url)
    except Exception as e:
        bot.reply_to(message, "الرسالة ممسوحة أو القناة المجموعة غير صحيحة.")
        ##print(e)
        return
    

def get_url_poll_2(message, amount):
    admins = db.get('admins')
    url = message.text
    x = checks(url)
    if x:
        channel, msg_id = x
    if not checks(url):
        bot.reply_to(message,text='• رجاء ارسل الرابط بشكل صحيح')
        return
    try:
        mm = "• ارسل الان تسلسل الإجابة في الاستفتاء\n\n• يجب ان يتراوح بين 0 : 9\n• علما بان اول اختيار يكون تسلسلة 0"
        x = bot.reply_to(message, mm, parse_mode='HTML')
        bot.register_next_step_handler(x, start_poll_2, amount, url)
    except Exception as e:
        bot.reply_to(message, "الرسالة ممسوحة أو القناة المجموعة غير صحيحة.")
        ##print(e)
        return
 
def start_poll_2(message, amount, url):
    stk.Add(message.from_user.id,"yes")
    num = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = poll_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'استفتاء'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : ')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    
    key = mk(
        [
            
            [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
        ]
        )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(poll_2(y['s'], url, int(num)))
           
            if x == 'o':
                continue
            if x == True:
                Mens += userbot_price
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
            
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
            
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return
def start_poll(message, amount, url):
    stk.Add(message.from_user.id,"yes")
    num = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = poll_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'استفتاء'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : ')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    
    key = mk(
        [
            
            [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
        ]
        )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(poll(y['s'], url, int(num)))
           
            if x == 'o':
                continue
            if x == True:
                Mens += userbot_price
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
            
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return

def get_rect_stories_url(message, amount, rec_list):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    if not check_url_stories(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    load_ = db.get('accounts_t')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تفاعلات ستوري'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ :')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(RECTION_STORIES(url,REACTIONS_LIST[rec_list],y))
            if x == True:
                Mens += userbot_price
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return

def get_view_stories_url(message, amount):
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    if not check_url_stories(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    load_ = db.get('accounts_t')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'مشاهدات ستوري '
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ :')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(WITH_STORIES(url, y))
            if x == True:
                Mens += userbot_price
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return

def get_view_url(message, amount):
    # ##print('vi 1')
    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'مشاهدات'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ :')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(view(y['s'], url))
           
            if x == 'o':
                continue
            if x == True:
                Mens += userbot_price
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return


def get_view_url_2(message, amount):
    ##print('vi 2')

    stk.Add(message.from_user.id,"yes")
    admins = db.get('admins')
    url = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'مشاهدات'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ :')
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true,Mens, false = 0,0,0
    key = mk(
    [
        
        [btn(text='إيقاف الطلب وإسترداد الرصيد♻️', callback_data='Stop1')]
    ]
    )
    for y in load_:
        res = stk.Get(message.from_user.id)
        if res=="no": 
            bot.send_message(message.chat.id, "تم الايقاف")
            break
        if true >= amount:
            break
        try:
            x = asyncio.run(view2(y['s'], url))
           
            if x == 'o':
                continue
            if x == True:
                Mens += userbot_price
                true += 1
            else:
                false += 1
            bot.edit_message_text(chat_id=message.chat.id,text=f"""⌁︙تم خصم ↫  {Mens} IQD من رصيدك 
⌁︙وبدأ رشق ↫ {amount}  لايك
⌁︙تم وصول ↫ {true}
⌁︙لم يصل ↫ {false}
⌁︙الرابط ↫⤈ {url}

""",message_id=v.message_id,reply_markup=key)
        except Exception as e:
            ##print(e)
            continue
    if true >= 1:
        
        acc['coins'] -= Mens
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {Mens}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return
def check_user(id):
    if not db.get(f'user_{id}'):
        return False
    return True

def set_user(id, data):
    db.set(f'user_{id}', data)
    return True

def get(id):
    ##print(db.get(f'user_{id}'))
    return db.get(f'user_{id}')

def delete(id):
    return db.delete(f'user_{id}')

def trend():
    k = db.keys("user_%")
    users = []
    for i in k:
        
        try:
            g = db.get(i[0])
            d = g["id"]
           
            users.append(g)
        except:
            continue
    data = users
    sorted_users = sorted(data, key=lambda x: len(x["users"]), reverse=True)
    result_string = "•<strong> المستخدمين الاكثر مشاركة لرابط الدعوى :</strong>\n"
    EOMJ = {
            0:'👑',
            1:'🏆',
            2:'🏅',
            3:'🎖',
        }
    EOMJ1 = {
        0:'🏆',
        1:'🥈',
        2:'🥉',
    }
    for key, user in enumerate(sorted_users[:4]):
        
        
        if len(user['users']) == 10:
            GivtPonts(user['id'],1000,len(user['users']))
        if len(user['users']) == 100:
            GivtPonts(user['id'],15000,len(user['users']))
        if len(user['users']) == 1000:
            GivtPonts(user['id'],120000,len(user['users']))
        # result_string += f"{EOMJ[key]}: ({len(user['users'])}) > {user['id']}\n"
        result_string += f"{EOMJ[key]}: ({len(user['users'])}) >  <a href='tg://user?id={user['id']}'> {user['id']}</a>\n"
    result_string +='• المستخدمين الأكثر نقاطاً في البوت \n'

    sorted_users2 = sorted(data, key=lambda x: int(x["coins"]), reverse=True)
    for key, user in enumerate(sorted_users2[:3]):
        result_string += f"{EOMJ1[key]} :( {user['coins']} ) > {user['id']} \n"

    return (result_string)


def detect(text):
    pattern = r'https:\/\/t\.me\/\+[a-zA-Z0-9]+'
    match = re.search(pattern, text)
    return match is not None
def casting(message):
    admins = db.get('admins')
    idm = message.message_id
    d = db.keys('user_%')
    good = 0
    bad = 0
    bot.reply_to(message, f'• جاري الاذاعة الى مستخدمين البوت الخاص بك ')
    for user in d:
        try:
            id = db.get(user[0])['id']
            bot.copy_message(chat_id=id, from_chat_id=message.from_user.id, message_id=idm)
            good+=1
        except:
            bad+=1
            continue
    bot.reply_to(message, f'• اكتملت الاذاعة بنجاح ✅\n• تم ارسال الى : {good}\n• لم يتم ارسال الى : {bad} ')
    return
def adminss(message, type):
    admins = db.get('admins')
    if type == 'add':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id in d:
            bot.reply_to(message, f'• هذا العضو ادمن بالفعل')
            return
        else:
            d.append(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اضافته بنجاح ✅')
            return
    if type == 'delete':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو ليس من الادمنية بالبوت')
            return
        else:
            d.remove(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اذالة العضو من الادمنية بنجاح ✅')
            return
    if type == 'change_price':
        nn = db.get(message.text) if db.exists(message.text) else "لا يوجد"
        x = bot.reply_to(message, f'⌁︙السعر الحالي لهذا المنتج : {nn}\n\n⌁︙ارسل السعر الجديد !')
        bot.register_next_step_handler(x, change_price, type)
def change_price(message, nn):
    try:
        new = int(message.text)
    except:
        bot.reply_to(message, f'ارسل رقم فقط')
        return
    db.set(f"{nn}", int(new))
    bot.reply_to(message, f'⌁︙تم تغيير سعر الخدمة : {nn}\n\n⌁ الى : {new}')
def banned(message, type):
    admins = db.get('admins')
    if type == 'ban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id in d:
            bot.reply_to(message, f'• هذا العضو محظور من قبل ')
            return
        else:
            d.append(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم حظر العضو من استخدام البوت')
            return
    if type == 'unban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو غير محظور ')
            return
        else:
            d.remove(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم الغاء حظر العضو بنجاح ✅')
            return
def get_info(message):
    id = message.text
    try:
        id = int(id)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    d = db.get(f'user_{id}')
    if not d:
        bot.reply_to(message, f'• هذا العضو غير موجود')
        return
    # {'id': user_id, 'users': [], 'coins': 0, 'paid': False}
    id, coins, users = d['id'], d['coins'], len(d['users'])
    bot.reply_to(message, f'• ايديه : {id}.\n• نقاطه: {coins} نقطة \n• عدد مشاركته لرابط الدعوة{users}')
    return
def send(message, tid):
    id = message.text
    if tid != USER_TEMP[message.from_user.id]['trans']['id']:
        return
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح ')
        return
    if not db.exists(f'user_{id}'):
        bot.reply_to(message, f'• هذا العضو غير موجود في البوت ❌')
        return
    if int(message.text) == int(message.from_user.id):
        bot.reply_to(message, f'• عذرا لا يمكنك تحويل نقاط لنفسك ❌')
        return
    if message.text == "/get_bot":
        bot.reply_to(message, f'{bbs}\n{bbb}')
        return
    x2 = bot.reply_to(message, f'• ارسل الان عدد النقاط التي تريد تحويلها لـ {id}')
    bot.register_next_step_handler(x2, get_amount_send, id, tid)
def get_info(message):
    id = message.text
    try:
        id = int(id)
    except:
        bot.reply_to(message, f'الايدي غلط ..')
        return
    d = db.get(f'user_{id}')
    if not d:
        bot.reply_to(message, f'مافي عضو..')
        return
    # {'id': user_id, 'users': [], 'coins': 0, 'paid': False}
    id, coins, users = d['id'], d['coins'], len(d['users'])
    bot.reply_to(message, f'لكيت العضو:\nايديه: {id} .\nنقاطه: {coins} نقطة .\nعدد الناس الى فايتين برابطه: {users}')
    return
def get_amount_send(message, id, tid):
    if tid != USER_TEMP[message.from_user.id]['trans']['id']:
        return
    amount = message.text
    try:
        amount = int(message.text)
    except:
        te = bot.reply_to(message, f'• الكمية يجب ان تكون عدد فقط ')
        return
    to_user = db.get(f'user_{id}')
    from_user = db.get(f'user_{message.from_user.id}')
    if amount < 1:
        bot.reply_to(message, f'• لا يمكن تحويل عدد اقل من 1')
        return
    if from_user['coins'] < amount:
        bot.reply_to(message, f'• نقاطك غير كافية لتحويل هذا المبلغ \n• تحتاج الى {amount-from_user["coins"]} نقطة')
        return
    from_user['coins']-=amount
    db.set(f'user_{message.from_user.id}', from_user)
    to_user['coins']+=amount
    db.set(f'user_{id}', to_user)
    try:
        bot.send_message(chat_id=id, text=f"• [👤] تم استلام {amount} من نقاط\n\n- من الشخص : {message.from_user.id}\n- نقاطك القديمة : {to_user['coins']}\n- نقاطك الان : {to_user['coins']+amount}")
    except: pass
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بارسال <strong>{amount}</strong> نقطة\n من <code>{message.from_user.id}</code> ..')
    bot.reply_to(message, f"• [👤] تم ارسال {amount} من نقاط\n\n- الى الشخص : {id}\n- نقاطك القديمة : {from_user['coins']}\n- نقاطك الان : {from_user['coins']-amount}")
    user_id = message.from_user.id
    trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
    count_trans = trans + 1
    db.set(f"user_{user_id}_trans", int(count_trans))
    return
def addpoints(message):
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    x = bot.reply_to(message, '• ارسل الان الكمية')
    bot.register_next_step_handler(x, addpoints_final, id)
def addpoints_final(message, id):
    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, f'يجب ان تكون الكمية ارقام فقط')
        return
    b = db.get(f'user_{id}')
    b['coins']+=amount
    db.set(f'user_{id}', b)
    bot.reply_to(message, f'تم بنجاح نقاطه الان : {b["coins"]} ')
    return
def setfo(message):
    users = message.text.replace('https://t.me/', '').replace('@',  '').split(' ')
    db.set('force', users)
    bot.reply_to(message, 'تمت بنجاح')
    return


def GivtPonts(id,pont,tg):
    GV = Givt()
    res = GV.Get(id)
   
    if res[1]=="false" and tg >= 10:
        ##print("10")
        threading.Thread(target=GV.Add,args=(id,"true",res[2],res[3])).start()
        
        b = db.get(f'user_{id}')
        b['coins']+=1000
        db.set(f'user_{id}', b)
        bot.send_message(id, f'• لقد حصلت على 1000 نقطة هدية 🎁 لأنك قم بدعوة {tg} عضو .')   
    if res[2]=="false" and tg >= 100:
        ##print("100")
        threading.Thread(target=GV.Add,args=(id,res[1],"true",res[3])).start()
       
        b = db.get(f'user_{id}')
        b['coins']+=15000
        db.set(f'user_{id}', b)
        bot.send_message(id, f'• لقد حصلت على 15000 نقطة هدية 🎁 لأنك قم بدعوة {tg} عضو .')   
    if res[3]=="false" and tg >= 1000:
        ##print("1000")
        threading.Thread(target=GV.Add,args=(id,res[1],res[2],"true")).start()
        
        b = db.get(f'user_{id}')
        b['coins']+=12000
        db.set(f'user_{id}', b)
        bot.send_message(id, f'• لقد حصلت على 12000 نقطة هدية 🎁 لأنك قم بدعوة {tg} عضو .')   

def vipp(message, type):
    if type == 'add':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get(f"user_{id}")
        if d is None:
            bot.reply_to(message, f'• العضو غير موجود في البوت')
            return
        d['premium'] = True
        db.set(f'user_{id}', d)
        x = bot.reply_to(message, f'• ارسل الان عدد الايام المتاحة للعضو ')
        bot.register_next_step_handler(x, addviptime, id)
        return
    if type == 'les':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get(f"user_{id}")
        if d is None:
            bot.reply_to(message, f'• العضو غير موجود في البوت')
            return
        d['premium'] = False
        db.set(f'user_{id}', d)
        bot.reply_to(message, f"تم انهاء الاشتراك الـ ᵛ͢ᵎᵖ للمستخدم {id}")

def addviptime(message,id):
    try:
        timenv = int(message.text)
    except:
        bot.reply_to(message, f"ارسل رقم فقط")
        return
    d = db.get(f"user_{id}")
    d['premium'] = True
    db.set(f'user_{id}', d)
    users = {}
    noww = time.time()
    users['vip'] = noww
    db.set(f'vip_{id}', users)
    db.set(f"vipp_{id}_time", int(timenv))
    us = bot.get_chat(id)
    if us.username is None:
        user = "لا يوجد"
    else:
        user = "@" + us.username
    name = us.first_name
    today = datetime.date.today()
    end_date = today + datetime.timedelta(days=int(timenv))
    now = datetime.datetime.now()
    HM = now.strftime("%p")
    if str(HM) == str("PM"):
        how = "مساءً"
    else:
        how = "صباحاً"
    hour = now.hour
    minutes = now.minute
    seconds = now.second
    d = int(timenv)
    h = int(timenv) * 24
    m = int(timenv) * 24 * 60
    s = int(timenv) * 24 * 60 * 60
    reb2 = f"""*• تهانينا ، تم تفعيل ᴠɪᴘ لحسابك في البوت ✅*\n\n*• مدة الاشتراك  ⏱️:*\n\n- المدة بالايام : {d}\n*• وقت انتهاء اشتراكك :*\n\n- يوم : {end_date}\n- الساعة : {hour} {how}\n- الدقيقة : {minutes}"""
    reb = f"""*• تمت عملية تفعيل ᴠɪᴘ جديده 🔥*
`{id}`
*• معلومات الاشتراك والمدة ⏱:*

_• وقت التفعيل :_

- اليوم : {today}
- الساعة : {hour} {how}
- الدقيقة : {minutes}

_• مدة الاشتراك  :_

- المدة بالايام : {d}
- المدة بالساعات : {h}
- المدة بالدقائق : {m}
- المدة بالثواني : {s}

*• وقت انتهاء الاشتراك :*

_• سينتهي اشتراك العضو في :_

- يوم : {end_date}
- الساعة : {hour} {how}
- الدقيقة : {minutes}"""
    bot.send_message(chat_id=int(sudo), text=reb, parse_mode="Markdown")
    bot.send_message(chat_id=int(id), text=reb2, parse_mode="Markdown")
def account(call):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.answer_callback_query(call.id, text="البوت قيد الصيانة والتطوير حاليا ⚙️",show_alert=True)
        return False
    cid, data, mid = call.from_user.id, call.data, call.message.id
    e = 5
    how = ""
    if e == 5:
        x = giiiift(cid)
        if x is not None:
            duration = datetime.timedelta(seconds=x)
            noww = datetime.datetime.now()
            target_datetime = noww + duration
            remaining_time = target_datetime - noww
            hours = remaining_time.seconds // 3600
            minutes = (remaining_time.seconds % 3600) // 60
            seconds = remaining_time.seconds % 60
            if hours > 0:
                how = f"{hours} ساعة"
            elif minutes > 0:
                how = f"{minutes} دقيقة"
            else:
                how = f"{seconds} ثانية"
        else:
            how = "يمكنك المطالبة بها 🎁"
        acc = get(cid)
        user_id = call.from_user.id
        coins, users = acc['coins'], len(get(cid)['users'])
        info = db.get(f"user_{call.from_user.id}")
        daily_count = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
        daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 30
        all_gift = daily_count * daily_gift
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
        prem = 'Premium' if info['premium'] == True else 'Free'
        codes = int(db.get(f"cd_{user_id}")) if db.exists(f"cd_{user_id}") else 0
        po = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
        textt = f'''
• 🗃️] معلومات حسابك 

• ❇️] عدد نقاط حسابك : {coins}
• ❇️] النقاط التي استخدمتها : {po}

• 🌀] عدد عمليات الاحاله التي قمت بها : {users}
• 👤] نوع اشتراكك داخل البوت : <code>{prem}</code>
• 📮] عدد الطلبات التي طلبتها : {buys}
• ♻️] عدد التحويلات التي قمت بها : {trans}

• ❇️] عدد النقاط اللي جمعتها من الهدايا اليومية : {all_gift}
• 💳] عدد اكواد الهدايا التي استخدمتها : {codes}
• 🎁] عدد الهدايا اليومية التي جمعتها : {daily_count}
• 🎁] متبقي علي الهدية : {how}'''
        keys = mk(row_width=2)
        btn1 = btn('الهدية اليومية 🎁', callback_data='dailygift')
        btn3 = btn('رابط الدعوة 🌀',callback_data='share_link')
        keys.add(btn3, btn1)
        keys.add(btn('‹ رجوع ↻›', callback_data='back'))
        bot.edit_message_text(text=textt,chat_id=cid,message_id=mid,reply_markup=keys)
def lespoints(message):
    if message.text == "/start":
        start_message(message)
        return
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    x = bot.reply_to(message, '• ارسل الان الكمية :')
    bot.register_next_step_handler(x, lespoints_final, id)
def lespoints_final(message, id):
    if message.text == "/start":
        start_message(message)
        return
    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, f'يجب ان تكون الكمية ارقام فقط')
        return
    b = db.get(f'user_{id}')
    b['coins']-=amount
    db.set(f'user_{id}', b)
    bot.reply_to(message, f'تم بنجاح نقاطه الان : {b["coins"]} ')
def check_dayy(user_id):
    users = db.get(f"user_{user_id}_giftt")
    noww = time.time()    
    WAIT_TIMEE = 24 * 60 * 60
    if db.exists(f"user_{user_id}_giftt"):
        last_time = users['timee']
        elapsed_time = noww - last_time
        if elapsed_time < WAIT_TIMEE:
            remaining_time = WAIT_TIMEE - elapsed_time
            return int(remaining_time)
        else:
            users['timee'] = noww
            db.set(f'user_{user_id}_giftt', users)
            return None
    else:
        users = {}
        users['timee'] = noww
        db.set(f'user_{user_id}_giftt', users)
        return None
    

def change_points(msg):
    link = msg.text
    if "https://t.me/EEObot?start=" not in str(link):
        bot.reply_to(msg, f"• برجاء ارسال رابط تحويل النقاط بشكل صحيح",reply_markup=bk)
        return
    try:
        forw = link.split("?start=")[1]
    except:
        bot.reply_to(msg, f"• برجاء ارسال رابط تحويل النقاط بشكل صحيح",reply_markup=bk)
        return
    x = asyncio.run(milliar(forw))
    if x == False:
        bot.reply_to(msg, f"- الرابط غير صحيح او انتهت مدة الرابط !",reply_markup=bk)
        return
    else:
        try:
            points = int(x)
        except:
            bot.reply_to(msg, f"• برجاء ارسال رابط تحويل النقاط بشكل صحيح",reply_markup=bk)
            return
        if points <500:
            bot.reply_to(msg, f"• عذرا ، الحد الادني لتحويل النقاط هو 500 نقطة ن بوت المليار",reply_markup=bk)
            return
        bef = points / 2
        b = db.get(f'user_{msg.from_user.id}')
        b['coins']+=int(bef)
        db.set(f'user_{msg.from_user.id}', b)
        bot.reply_to(msg, f"• تم بنجاح عملية تحويل {points} نقطة ✅\n\n• تم اضافة {int(bef)} نقطة الى حسابك بنجاح ✅",reply_markup=bk)

def get_amount_tom_view(message, amount):
    try:
        count = int(message.text)
    except:
        x = bot.reply_to(message,text=f'• رجاء ارسل عدد المنشورات بشكل صحيح')
        return
    all = count * int(amount)
    acc = db.get(f'user_{message.from_user.id}')
    if int(all) > acc['coins']:
        bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{all}</strong> نقطة')
        return
    x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n• عدد المنشورات : {count}\n\n• ارفع الان البوت @hdrtyrdbot ادمن في قناتك ، ثم قم باعادة توجيه اي رسالة من القناة الى البوت')
    bot.register_next_step_handler(x, get_amount_tom_view_forward, amount, count)
######################### rad edit rect
def get_amount_tom_rect(message, amount):
    try:
        count = int(message.text)
    except:
        x = bot.reply_to(message,text=f'• رجاء ارسل عدد المنشورات بشكل صحيح')
        return
    all = count * int(amount)
    acc = db.get(f'user_{message.from_user.id}')
    if int(all) > acc['coins']:
        bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الى  <strong>{all}</strong> نقطة')
        return
    x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n• عدد المنشورات : {count}\n\n• ارفع الان البوت @hdrtyrdbot ادمن في قناتك ، ثم قم باعادة توجيه اي رسالة من القناة الى البوت')
    bot.register_next_step_handler(x, get_amount_tom_rect_forward, amount, count)

def get_amount_tom_rect_forward(message, amount, count):
    if message.forward_from_chat:
        forward_chat_type = message.forward_from_chat.type
        if forward_chat_type == 'channel':
            user = "@" + message.forward_from_chat.username
            username = message.forward_from_chat.username
            chat_member = bot.get_chat_member(user, bot.get_me().id)
            if str(chat_member.status) == "administrator":
                db.set(f"tom_r_{username}", int(count))
                db.set(f"type_r_{username}", "view")
                db.set(f"amount_r_{username}", int(amount))
                tom_ch = db.get("tom_r_ch") if db.exists("tom_r_ch") else []
                tom_ch.append(username)
                db.set("tom_r_ch", tom_ch)
                bot.reply_to(message, text='• تم حفظ القناة بنجاح ، سيتم تنفيذ طلبك تلقائيا')
                all = int(count) * int(amount)
                acc = db.get(f'user_{message.from_user.id}')
                acc['coins'] -= all
                db.set(f'user_{message.from_user.id}', acc)
            else:
                bot.reply_to(message, text='• عذرا ، البوت غير مشرف في هذه القناة')
                return
        else:
            bot.reply_to(message, text='• رجاء قم باعادة توجية الرسالة من القناة بشكل صحيح')
            return
    else:
        bot.reply_to(message, text='• رجاء قم باعادة توجية الرسالة من القناة بشكل صحيح')
        return

#############################
def get_amount_tom_view_forward(message, amount, count):
    if message.forward_from_chat:
        forward_chat_type = message.forward_from_chat.type
        if forward_chat_type == 'channel':
            user = "@" + message.forward_from_chat.username
            username = message.forward_from_chat.username
            chat_member = bot.get_chat_member(user, bot.get_me().id)
            if str(chat_member.status) == "administrator":
                db.set(f"tom_{username}", int(count))
                db.set(f"type_{username}", "view")
                db.set(f"amount_{username}", int(amount))
                tom_ch = db.get("tom_ch") if db.exists("tom_ch") else []
                tom_ch.append(username)
                db.set("tom_ch", tom_ch)
                bot.reply_to(message, text='• تم حفظ القناة بنجاح ، سيتم تنفيذ طلبك تلقائيا')
                all = int(count) * int(amount)
                acc = db.get(f'user_{message.from_user.id}')
                acc['coins'] -= all
                db.set(f'user_{message.from_user.id}', acc)
            else:
                bot.reply_to(message, text='• عذرا ، البوت غير مشرف في هذه القناة')
                return
        else:
            bot.reply_to(message, text='• رجاء قم باعادة توجية الرسالة من القناة بشكل صحيح')
            return
    else:
        bot.reply_to(message, text='• رجاء قم باعادة توجية الرسالة من القناة بشكل صحيح')
        return
        
############

@bot.channel_post_handler(func=lambda message: True , content_types=['text', 'photo', 'video', 'audio'])
def handle_new_channel_post(message):
    tom_ch = db.get("tom_ch") if db.exists("tom_ch") else []
    tom_r_ch = db.get("tom_r_ch") if db.exists("tom_r_ch") else []
    # print('on message 1')
    if message.chat.username not in tom_ch and message.chat.username not in tom_r_ch:
        return
    # print('on message 2')
    
    if message.chat.username in tom_r_ch:
        count = int(db.get(f"tom_r_{message.chat.username}"))
        type = db.get(f"type_r_{message.chat.username}")
        amount = db.get(f"amount_r_{message.chat.username}")
        load_ = db.get('accounts')
        true = 0
        false = 0

        if count <=1:
            tom_ch = db.get("tom_r_ch") if db.exists("tom_r_ch") else []
            tom_ch.remove(message.chat.username)
            db.set("tom_r_ch",tom_ch)
            return
        
        channel = message.chat.username
        msg_id = message.message_id
        for y in load_:
            if true >= amount:
                break
            try:

                x = asyncio.run(tom_rect(y['s'], channel, msg_id))
            except Exception as e:
                # print(e)
                pass
                # return
        count = int(db.get(f"tom_{message.chat.username}"))
        aft = count - 1
        db.set(f"tom_{message.chat.username}", aft)
        
    
    if message.chat.username in tom_ch:
        count = int(db.get(f"tom_{message.chat.username}"))
        type = db.get(f"type_{message.chat.username}")
        amount = db.get(f"amount_{message.chat.username}")
        load_ = db.get('accounts')
        true = 0
        false = 0
        
        if count <=1:
            tom_ch = db.get("tom_ch") if db.exists("tom_ch") else []
            tom_ch.remove(message.chat.username)
            db.set("tom_ch",tom_ch)
            return
        
        channel = message.chat.username
        msg_id = message.message_id
        for y in load_:
            if true >= amount:
                break
            try:

                x = asyncio.run(tom_view(y['s'], channel, msg_id))
            except Exception as e:
                # print(e)
                pass
                # return
        count = int(db.get(f"tom_{message.chat.username}"))
        aft = count - 1
        db.set(f"tom_{message.chat.username}", aft)
        

 
 
def entre_bot(message):
    try:
        it = int(message.text)
        bot.reply_to(message, f"تم تغيير عدد النقاط الى {it}",reply_markup=bk)
        db.set("entre_bot", it)
    except:
        bot.reply_to(message, f"ارسل رقم فقط عزيزي",reply_markup=bk)
def get_story_url(message, amount):
    if "/s/" in message.text:
        try:
            link = message.text
            url = f"https://kd1s.com/api/v2?key=231dccbbc91510db5cf78e4f38cf489c&action=add&service=11465&quantity={amount}&link={link}"
            v2 = requests.get(url)
            data = v2.json()
            order = data['order']
            viewff = member_price * amount
            user_info = db.get(f"user_{message.from_user.id}")
            user_info['coins'] = int(user_info['coins']) - int(viewff) 
            db.set(f"user_{message.from_user.id}", user_info)
            bot.reply_to(message, text=f"""• بدء تنفيذ طلبك بنجاح ( رشق مشاهدات ستورى ) ✅
• الرابط : {link}
• الكمية : {amount}
• ايدي الطلب : {order}

• تم خصم :  {viewff} من نقاطك 
• اصبحت نقاطك : {user_info['coins']}""")
        except Exception as e:
            bot.reply_to(message, text=f"خطا غير متوقع : {e}")

def get_code_coin(message, ids):
    if USER_TEMP[message.from_user.id]['code']['id'] != ids:
        return 
    code = message.text
    if not datas.CODE_EXISTS(code):
        bot.send_message(text='عذرا الكود غير صحيح او انتهت صلاحيتة ! ', chat_id=message.chat.id)
        return
    cods_data = datas.GET_DATA()

    if message.from_user.id in cods_data['code'][code]['users']:
        bot.send_message(text='عذرا لا يمكنك استخدام الكود اكثر من مرة ! ', chat_id=message.chat.id)
        return
    from_user = db.get(f'user_{message.from_user.id}')
    from_user['coins']+=cods_data['code'][code]['coin']
    db.set(f'user_{message.from_user.id}', from_user)
    bot.send_message(text='تم اضافة لي حسابك : {} نفطة .'.format(cods_data['code'][code]['coin']), chat_id=message.chat.id)
    cods_data['code'][code]['mem']-=1 
    cods_data['code'][code]['users'].append(message.from_user.id) 
    if cods_data['code'][code]['mem'] == 0:
        cods_data['code'].pop(code)
    datas.UPDATE_DATA(cods_data)
    

def hand_get_code(message):
    code = message.text
    ms = bot.send_message(text='قم بي ارسال عدد النقاط', chat_id=message.chat.id)

    bot.register_next_step_handler(ms, hand_get_code_coin, code)


def hand_get_code_coin(message, code):
    try:
        coin = int(message.text)
    except:
        bot.send_message(text='يرجا ارسال ارقام بدون احرف .', chat_id=message.chat.id)
        return
    ms = bot.send_message(text='قم بي ارسال عدد الاعضاء', chat_id=message.chat.id)
    bot.register_next_step_handler(ms, hand_get_code_mem, code,coin)
    

def hand_get_code_mem(message, code, coin):
    try:
        mem = int(message.text)
    except:
        bot.send_message(text='يرجا ارسال ارقام بدون احرف .', chat_id=message.chat.id)
        return
    
    datas.NEW_CODE(code, coin, mem)
    bot.send_message(chat_id=message.chat.id, text=''' تم انشاء كودك بي نجاج . \nالكود : `{}` \nعدد النقاط : {} \nعدد الاعضاء : {}'''.format(code, coin, mem))

def make_code_coin(message):
    try:
        coin = int(message.text)
    except:
        bot.send_message(text='يرجا ارسال ارقام بدون احرف .', chat_id=message.chat.id)
        return
    from_user = db.get(f'user_{message.from_user.id}')

    if from_user['coins'] < coin:
        bot.send_message(text='لا يوجد لديك نقاط كافي .', chat_id=message.chat.id)
        return 
    
    if coin < 100:
        bot.send_message(text='عذرا اقل عدد للتحويل 100 نقطة ', chat_id=message.chat.id)
        return 
    
    CODE = RAND_CODE()
    from_user = db.get(f'user_{message.from_user.id}')
    from_user['coins'] -= coin
    print(from_user)
    db.set(f'user_{message.from_user.id}', from_user)
    datas.NEW_USER_CODE(CODE ,coin, message.from_user.id)

    bot.send_message(chat_id=message.chat.id, text='''تم انشاء كودك بنجاح \n\n - الكود : `{}` \n- عدد النقاط : {}\n\n'''.format(CODE, coin), parse_mode='Markdown')

def BAND_CHAT(channel_username: str):
    user_id = db.get(f'id_{channel_username}')
    chats_dd = db.get('force_ch')
    chats_dd.remove(channel_username)
    db.set('force_ch', chats_dd)
    balcklist = db.get('chat_blacklist')
    balcklist.append(channel_username)
    db.set('chat_blacklist', balcklist)
    bot.send_message(text=f'تم ايقاف تمويل قناتك ( {channel_username} ) من قبل المطور بسبب مخالفة قوانين البوت .', chat_id=user_id)    

def ad_gets(msg):
    id = randid()
    ad_temp.update({id:{'msg':msg.text,'user_id':msg.from_user.id}})
    keys = mk(row_width=2)
    keys.add(btn(text='الغاء', callback_data='ps'), btn(text='موافق ', callback_data=f'ad_send|{id}'))
    bot.send_message(chat_id=msg.chat.id, text='اهل انت متائكد من نشر الاعلان سيتم خصم 1000 نقطة من رصيدك . ',reply_markup=keys)


@bot.message_handler(func= lambda m: m.text.split(' ')[0] in COMMAND_PRIC.keys())
def EDIT_PEIC(message):
    try:
        PRIC = int(message.text.split(' ')[1])
    except:
        bot.send_message(text='يرجا ارسال السعر ارقام بدون احرف .', chat_id=message.chat.id)
        return
    data = json.load(open('./datas/prices.json', 'r'))
    data[COMMAND_PRIC[message.text.split(' ')[0]]] = PRIC
    with open('./datas/prices.json', 'w') as JSObj:
        json.dump(data, JSObj, indent=3)
    bot.send_message(text='تم تغير سعر الخدمة بنجاح', chat_id=message.chat.id)

def get_url_click_force(message):
    xx = checks(message.text)
    if not xx:
        bot.reply_to(message, "• ارسل رابط المنشور بشكل صحيح.")
        return
    load_ = db.get("accounts")
    session = random.choice(load_)
    o = asyncio.run(get_msgs(session['s'], message.text))
    print(o)
    if not o:
        bot.reply_to(message, "• ارسل رابط المنشور بشكل صحيح.")
        return
    res = isinstance(o, list)
    if not res:
        bot.reply_to(message, "• ارسل رابط المنشور بشكل صحيح.")
        return
    keys = mk()
    for text in o:
        btn1 = btn(text=text, callback_data=f"V-{text}-{message.text}")
        keys.add(btn1)
    keys.add(btn('رجوع ', callback_data='back'))
    bot.reply_to(message, "اختر الزر الذي تريد رشقه", reply_markup=keys)
def get_amount_click_force(message, text, url):
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
        return
    if amount < 1:
        bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>0</strong> ..',reply_markup=bk)
        return
    if amount > 2000:
        bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
        return
    pr = vote_price * amount
    acc = db.get(f'user_{message.from_user.id}')
    if int(pr) > acc['coins']:
        bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
        return
    x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• الان ارسل وقت الإنتضار بين الرشق (بالثواني) \n\n• ارسل 0 اذا كنت تريده فوري\n• يجب ان لايزيد عن 200')
    bot.register_next_step_handler(x, get_time_click_force, amount, text, url)
    return

def get_time_click_force(message, amount, text, url):
    try:
        time = int(message.text)
    except:
        x = bot.reply_to(message,text=f'• رجاء ارسل الوقت بشكل صحيح')
        return
    if time <0:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    if time >200:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    pr = vote_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تصويت'
    db.set(f"serv_{message.from_user.id}", True)
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}\n• الوقت بين التصويت : {time} ')
    true, false = 0, 0
    tmmmm = 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• تم بدء طلبك بنجاح ✅\n\n• العدد : {amount}\n• يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            x = asyncio.run(click_force(y['s'], text, url, time))
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        acc = db.get(f'user_{message.from_user.id}')
        for ix in range(true):
            acc['coins'] -= vote_price
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {amount*vote_price}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return
    
try:
    bot.infinity_polling()
    bot2.infinity_polling()
except:
    pass




