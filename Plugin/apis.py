from pyrogram import Client, enums
import re, asyncio
from kvsqlite.sync import Client as uu
import random 
from pyrogram.raw import functions
from time import sleep

from telethon import TelegramClient, functions as functele ,events, types
from telethon.errors.rpcerrorlist import UserDeactivatedBanError
from telethon.sessions import StringSession

db = uu('elhakem.ss', 'rshq')

def detect(text):
    pattern = r'https:\/\/t\.me\/\+[a-zA-Z0-9]+'
    match = re.search(pattern, text)
    return match is not None

def check_format(link):
    pattern = r"https?://t\.me/(\w+)/(\d+)"
    match = re.match(pattern, link)
    
    if match:
        username = match.group(1)
        post_id = int(match.group(2))
        return username, post_id
    else:
        return False

async def join_chat(session: str, chat: str):
    c = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    try:
        await c.start()
    except:
        return False
    if db.exists(f'issub_{session[:15]}_{chat}'): return 'o'
    try:
        await c.join_chat(chat)
        db.set(f'issub_{session[:15]}_{chat}', True)
    except Exception as e:
        print(e)
        await c.stop()
        return False
    await c.stop()
    return True
async def leave_chats(session: str):
    c = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    try:
        await c.start()
    except:
        return False
    types = ['ChatType.CHANNEL', 'ChatType.SUPERGROUP', 'ChatType.GROUP']
    
    async for dialog in c.get_dialogs():
        if str(dialog.chat.type) in types:
            id = dialog.chat.id
            try:
                await c.leave_chat(id)
                await asyncio.sleep(2.5)
            except:
                continue
        else:
            continue
    await c.stop()
    return True
async def leave_chat(session: str, chat: str):
    c = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    try:
        await c.start()
    except:
        return False
    try:
        await c.leave_chat(chat)
    except Exception as e:
        print(e)
        await c.stop()
        return False
    await c.stop()
    return True

async def send_message(session:str, chat:str, text: str):
    c = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    try:
        await c.start()
    except Exception as e:
        print(e)
        return False
    info = None
    if detect(chat):
        print('ok')
        try:
            try:
                id = await c.join_chat(chat)
            except:
                pass
            try:
                info = await c.get_chat(chat)
            except Exception as e:
                await c.stop()
                return False
        except Exception as e:
            await c.stop()
            return False
    else:
        chat = chat.replace('https://t.me/', '').replace('t.me', '').replace('@', '').replace('.', '')
        print(chat)
        try:
            info = await c.get_chat(chat)
            print(info)
        except Exception as e:
            print(e)
            await c.stop()
            return False
    if info:
        type = None
        allowed = ['bot', 'user', 'group', 'super', 'bot']
        if info.type == enums.ChatType.BOT:
            type = 'bot'
        if info.type == enums.ChatType.PRIVATE:
            type = 'user'
        if info.type == enums.ChatType.GROUP:
            type = 'group'
        if info.type == enums.ChatType.SUPERGROUP:
            type = 'super'
        if type in allowed:
            if type == 'bot':
                try:
                    await c.send_message(chat_id=info.id, text=text)
                except Exception as e:
                    print(e)
                    return False
                await c.stop()
                return True
            if type == 'group':
                try:
                    await c.send_message(chat_id=info.id, text=text)
                except:
                    return False
                try:
                    await c.leave_chat(info.id)
                except:
                    pass
                await c.stop()
                return True
            if type == 'super':
                try:
                    await c.send_message(chat_id=info.id, text=text)
                except:
                    return False
                try:
                    await c.leave_chat(info.id)
                except:
                    pass
                await c.stop()
                return True
            if type == 'user':
                try:
                    await c.send_message(chat_id=info.id, text=text)
                    
                except Exception as e:
                    print(e)
                    return False
                await c.stop()
                return True
        else:
            return False
    else:
        return False

async def vote_one(session, link, time):
    c = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    try:
        await c.start()
    except:
        return False
    if db.exists(f'isvote_{session[:15]}_{link}'): return 'o'
    x = check_format(link)
    if x:
        username, id = x
        try:
            msg = await c.get_messages(chat_id=username, message_ids=[int(id)])
        except Exception as e:
            print(e)
            await c.stop()
            return False
        if msg[0].reply_markup:
            await c.join_chat(username)
            button = msg[0].reply_markup.inline_keyboard[0][0].text
            await asyncio.sleep(time)
            result = await msg[0].click(button)
            if result:
                db.set(f'isvote_{session[:15]}_{link}', True)
                return True
            else:
                db.set(f'isvote_{session[:15]}_{link}', True)
                await c.stop()
                return True
        else:
            await c.stop()
            return False
    else:
        await c.stop()
        return False
    

async def vote_one_and_veos(session, link, time):
    c = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    try:
        await c.start()
    except:
        return False
    if db.exists(f'isvote_{session[:15]}_{link}'): return 'o'
    x = check_format(link)
    if x:
        username, id = x
        try:
            msg = await c.get_messages(chat_id=username, message_ids=[int(id)])
        except Exception as e:
            print(e)
            return False
        if msg[0].reply_markup:
            await c.join_chat(username)
            button = msg[0].reply_markup.inline_keyboard[0][0].text
            await asyncio.sleep(time)
            result = await msg[0].click(button)
            if result:
              
                z = await c.invoke(functions.messages.GetMessagesViews(
                            peer= (await c.resolve_peer(username)),
                            id=[int(id)],
                            increment=True
                ))
                db.set(f'isvote_{session[:15]}_{link}', True)
                await c.stop()
                return True
            else:
                db.set(f'isvote_{session[:15]}_{link}', True)
                await c.stop()
                return True
        else:
            await c.stop()
            return False
    else:
        await c.stop()
        return False
    

async def vote_one_and_3(session, link, time):
    rs = ["👍","🤩","🎉","🔥","❤️","🥰","🥱","🥴","🌚","🍌","💔","🤨","😐","🖕","😈","👎","😁","😢","💩","🤮","🤔","🤯","🤬","💯","😍","🕊","🐳","🤝","👨","🦄","🎃","🤓","👀","👻","🗿","🍾","🍓","⚡️","🏆","🤡","🌭","🆒","🙈","🎅","🎄","☃️","💊"]
    c = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    try:
        await c.start()
    except:
        return False
    if db.exists(f'isvote_{session[:15]}_{link}'): return 'o'
    x = check_format(link)
    if x:
        username, id = x
        try:
            msg = await c.get_messages(chat_id=username, message_ids=[int(id)])
        except Exception as e:
            print(e)
            await c.stop()
            return False
        if msg[0].reply_markup:
            await c.join_chat(username)
            button = msg[0].reply_markup.inline_keyboard[0][0].text
            await asyncio.sleep(time)
            result = await msg[0].click(button)
            await c.send_reaction(username, int(id), random.choice(rs))
            if result:
                db.set(f'isvote_{session[:15]}_{link}', True)
                await c.stop()
                return True
            else:
                db.set(f'isvote_{session[:15]}_{link}', True)
                await c.stop()
                return True
        else:
            await c.stop()
            return False
    else:
        await c.stop()
        return False
    
async def reactions(session, link, like):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    if db.exists(f'isreact_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.send_reaction(channel, msg_id, like)
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
async def reaction(session, link):
    rs = ["👍","🤩","🎉","🔥","❤️","🥰","🥱","🥴","🌚","🍌","💔","🤨","😐","🖕","😈","👎","😁","😢","💩","🤮","🤔","🤯","🤬","💯","😍","🕊","🐳","🤝","👨","🦄","🎃","🤓","👀","👻","🗿","🍾","🍓","⚡️","🏆","🤡","🌭","🆒","🙈","🎅","🎄","☃️","💊"]
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    if db.exists(f'isreact_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.send_reaction(channel, msg_id, random.choice(rs))
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
async def forward(session, link):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.forward_messages('me', channel, [msg_id])
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
    

async def view2(session, link):
    rs = ["👍","🤩","🎉","🔥","❤️","🥰","🥱","🥴","🌚","🍌","💔","🤨","😐","🖕","😈","👎","😁","😢","💩","🤮","🤔","🤯","🤬","💯","😍","🕊","🐳","🤝","👨","🦄","🎃","🤓","👀","👻","🗿","🍾","🍓","⚡️","🏆","🤡","🌭","🆒","🙈","🎅","🎄","☃️","💊"]
 
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    if db.exists(f'isview_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.send_reaction(channel, int(msg_id), random.choice(rs))
        z = await client.invoke(functions.messages.GetMessagesViews(
                    peer= (await client.resolve_peer(channel)),
                    id=[int(msg_id)],
                    increment=True
        ))
        db.set(f'isview_{session[:15]}_{link}', True)
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
    
   
async def view(session, link):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    if db.exists(f'isview_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        z = await client.invoke(functions.messages.GetMessagesViews(
                    peer= (await client.resolve_peer(channel)),
                    id=[int(msg_id)],
                    increment=True
        ))
        db.set(f'isview_{session[:15]}_{link}', True)
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
    


async def poll(session, link, pi):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    if db.exists(f'ispoll_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.vote_poll(channel, msg_id, [pi])
        db.set(f'ispoll_{session[:15]}_{link}', True)
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
    

   
async def poll_2(session, link, pi):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    if db.exists(f'ispoll_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        info = await client.get_chat(channel)
        await client.vote_poll(channel, msg_id, [pi])
        db.set(f'ispoll_{session[:15]}_{link}', True)
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
async def userbot(session, user):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    try:
        await client.send_message(user, "/start")
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
async def linkbot(session, user, text):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    try:
        await client.send_message(user, text)
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
async def linkbot2(session, user, text, channel_force):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    try:
        await client.join_chat(channel_force)
        await client.send_message(user, text)
        await client.leave_chat(channel_force)
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
async def check_chat(session: str, link: str):
    c = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881, no_updates=True,workers=2, session_string=session)
    try:
        await c.start()
    except:
        return False
    x = check_format(link)
    if x:
        username, id = x
        try:
            x = await c.get_chat(username)
        except:
            await c.stop()
            return False
        await c.stop()
        return True
    else:
        await c.stop()
        return False
async def send_comment(session, url, text):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    x = check_format(url)
    if x:
        channel, msg_id = x
    try:
        await client.join_chat(channel)
        await client.send_message(channel, text, reply_to_message_id=msg_id)
        await client.leave_chat(channel)
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
        
async def leave_chats(session):
    c = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    try:
        await c.start()
    except:
        return False
    types = ['ChatType.CHANNEL', 'ChatType.SUPERGROUP', 'ChatType.GROUP']
    ty = ['ChatType.BOT']
    async for dialog in c.get_dialogs():
        if str(dialog.chat.type) in types:
            id = dialog.chat.id
            try:
                await c.leave_chat(id)
                await asyncio.sleep(2)
            except:
                continue
        else:
            if str(dialog.chat.type) in ty:
                id = dialog.chat.id
                try:
                    await c.block_user(id)
                    await asyncio.sleep(2)
                    print("Done")
                except Exception as e:
                    print(e)
                    continue
            else:
                continue
    await c.stop()
    return True
async def join_chatp(session, invite_link):
    c = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await c.start()
    print(invite_link)
    try:
        chat = await c.join_chat(invite_link)
        await c.stop()
        return True
    except Exception as e:
        print('An error occurred:', str(e))
        await c.stop()
        return False
    

async def dump_votess(session, link):
    c = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    try:
        await c.start()
    except:
        return False
    if not db.exists(f'isvote_{session[:15]}_{link}'): return 'o'
    x = check_format(link)
    if x:
        username, id = x
        try:
            await c.join_chat(username)
            msg = await c.get_messages(chat_id=username, message_ids=[int(id)])
        except Exception as e:
            print(e)
            return False
        if msg[0].reply_markup:
            
            button = msg[0].reply_markup.inline_keyboard[0][0].text
            result = await msg[0].click(button)
            if result:
                db.delete(f'isvote_{session[:15]}_{link}')
            else:
                return False
        else:
            return False
    else:
        return False
    

async def clear(bot ,id):
    if not db.exists('accounts'):
        bot.send_message(id,'• لا يوجد اي ارقام في البوت الخاص بك')
        return
    
    sessions = db.get('accounts')
    if len(sessions) < 1:
        bot.send_message(id,'لا يوجد اي ارقام في البوت الخاص بك')
        return
    
    deleted_count = 0
    working_count = 0
    print(len(sessions))
    bot.send_message(id,'• برجاء الانتظار \n• جارى بدء عملية التنظيف')
    
    updated_sessions = []
    
    for session in sessions:
        sessio = session['s']
        phon = session['phone']
        try:
            client = Client('::memory::', api_id=22119881, api_hash='95f5f60466a696e33a34f297c734d048', in_memory=True, session_string=sessio)
            sleep(3)
        except Exception as a:
            print(a)
            continue
        
        try:
            await client.start()
        except Exception as a:
            print(a)
            deleted_count += 1
            continue
        
        try:
            await client.get_me()
            working_count += 1
            updated_sessions.append({"s":sessio, 'phone': phon})
        except Exception as a:
            print(a)
            deleted_count += 1
    db.set("accounts", updated_sessions)
    bot.send_message(id,f'• تم انتهاء فحص وتنظيف الحسابات ♻️\n\n• الحسابات التي تعمل ✅ : {working_count} \n\n• الحسابات التي لا تعمل ❌ : {deleted_count}')
    return

async def Convert_Sessions(bot, id: int):
    sessions = db.get('accounts')
    if len(sessions) < 1:
        bot.send_message(id,'لا يوجد اي ارقام في البوت الخاص بك لي يتم تحويلها ')
        return
    
    ConverDone = []
    Done_Crove = 0
    bot.send_message(id,'Start Conver Sessions .')

    for session in sessions:
        Done_Crove+=1
        session_string = session['s']
        Convert_sess = MangSession.PYROGRAM_TO_TELETHON(session_string)
        ConverDone.append(Convert_sess)

    db.set('accounts_t', ConverDone)
    bot.send_message(id,f'Done Convert : {Done_Crove} acconets')



async def milliar(link):
    points = None
    
    async def handle_message(event):
        nonlocal points
        if "تم اضافة" in str(event.message.text):
            x = event.message.text
            start_index = x.find("تم اضافة **") + len("تم اضافة **")
            end_index = x.find("** نقاط", start_index)
            points = int(x[start_index:end_index].strip())
            print(points)
            await client.disconnect()
        else:
            points = False
            await client.disconnect()
    try:
        client = TelegramClient('session', 29848011, 'ab9bd73716cfe9939ea5ff0bd9bad498')
        try:
            await client.connect()
        except:
            await client.disconnect()
            await client.connect()
        
        try:
            await client.send_message('eeobot', f"/start {link}")
            client.add_event_handler(handle_message, events.NewMessage(from_users='eeobot'))
            await client.run_until_disconnected()
        except Exception as e:
            print(e)
            return False
    except Exception as e:
        print(e)
        pass
    return points

async def force_vote(session, invite_link, msg_id, time):
    c = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    try:
        await c.start()
    except Exception as e:
        print(e)
        return False
    
    if db.exists(f'isvote_{session[:15]}_{invite_link}{msg_id}'): 
        return 'o'

    try:
        await c.join_chat(invite_link)
    except Exception as e:
        print(e)
        return False

    try:
        chat = await c.get_chat(invite_link)
        chat_id = chat.id
        msg = await c.get_messages(chat_id=chat_id, message_ids=[int(msg_id)])
    except Exception as a:
        print(a)
        return False
    if msg[0].reply_markup:
        await c.send_message('me', text=".")
        button = msg[0].reply_markup.inline_keyboard[0][0].text
        await asyncio.sleep(time)
        result = await msg[0].click(button)
        if result:
            db.set(f'isvote_{session[:15]}_{invite_link}{msg_id}', True)
            await c.stop()
            return True
        else:
            db.set(f'isvote_{session[:15]}_{invite_link}{msg_id}', True)
            await c.stop()
            return True
    else:
        return False

async def positive(session, link):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    if db.exists(f'isreact_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        rs = ["👍","❤","🔥","😍","🤩"]
        await client.send_reaction(channel, msg_id, random.choice(rs))
        await client.stop()
        db.set(f'ispoll_{session[:15]}_{link}', True)
        return True
    except:
        await client.stop()
        return False
        
async def negative(session, link):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    if db.exists(f'isreact_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        rs = ["👎","💩","🤮","🤬","🖕"]
        await client.send_reaction(channel, msg_id, random.choice(rs))
        await client.stop()
        db.set(f'ispoll_{session[:15]}_{link}', True)
        return True
    except:
        await client.stop()
        return False
    


async def tom_rect(session, channel,msg_id):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    try:
        rs = ["👍","❤","🔥","😍","🤩"]
        await client.send_reaction(channel, msg_id, random.choice(rs))
        await client.stop()
        return True
    except:
        await client.stop()
        return False
    
async def tom_view(session, channel,msg_id):
    client = Client('::memory::', in_memory=True, api_hash='95f5f60466a696e33a34f297c734d048', api_id=22119881,lang_code="ar", no_updates=True,workers=2, session_string=session)
    await client.start()
    try:
        z = await client.invoke(functions.messages.GetMessagesViews(
                    peer= (await client.resolve_peer(channel)),
                    id=[int(msg_id)],
                    increment=True
        ))
        await client.stop()
        return True
    except:
        await client.stop()
        return False

async def WITH_STORIES(url: str, session: str, api_hash: str = '95f5f60466a696e33a34f297c734d048',api_id: int = 22119881):
    try:
        url_split = url.split('/')
        username = url_split[-3]
        peer_id = int(url_split[-1])
    except:
        pass
    try:
        # print('connect 1')
        app = TelegramClient(StringSession(session), api_id=api_id, api_hash=api_hash, entity_cache_limit=2)
        await app.connect()      
        # print('connect 2')
        result = await app(functele.stories.ReadStoriesRequest(
            peer=username, 
            max_id=peer_id
        ))
        await app.disconnect()

        return True

    except Exception as a:
        print(a)
        return False


async def RECTION_STORIES(url: str, reactions_list: list,session: str, api_hash: str = '95f5f60466a696e33a34f297c734d048',api_id: int = 22119881):
    try:
        url_split = url.split('/')
        username = url_split[-3]
        peer_id = int(url_split[-1])
    except:
        pass
    try:
        app = TelegramClient(StringSession(session), api_id=api_id, api_hash=api_hash, entity_cache_limit=2)
        await app.start() 
        result = await app(functele.stories.SendReactionRequest(
                peer=username,
                story_id=peer_id,
                reaction=types.ReactionEmoji(
                    emoticon=random.choices(reactions_list)[0]
                ),
                add_to_recent=True
            ))
        await app.stop()
        return True
        
    except Exception as a:
        print(a)
        return False

async def get_msgs(session, link):
    c = Client('::memory::', in_memory=True, api_hash='4f9f53e287de541cf0ed81e12a68fa3b', api_id=22256614,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except Exception as a:
        print(a)
        return False
    x = check_format(link)
    if x:
        username, id = x
        try:
            msg = await c.get_messages(chat_id=username, message_ids=[int(id)])
        except Exception as a:
            print(f"hhhh»»»»» {a}")
            await c.stop()
            return False
        if msg[0].reply_markup:
            button = msg[0].reply_markup.inline_keyboard[0]
            results = []
            for btn in button:
                results.append(str(btn.text))
            return results
        else:
            await c.stop()
            return False
    else:
        await c.stop()
        return False

async def click_force(session, text, link, time):
    c = Client('::memory::', in_memory=True, api_hash='4f9f53e287de541cf0ed81e12a68fa3b', api_id=22256614,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except Exception as e:
        print(e)
        return False
    if db.exists(f'isvote_{session[:15]}_{link}'):
        await c.stop()
        return 'o'
    x = check_format(link)
    if x:
        username, id = x
        try:
            msg = await c.get_messages(chat_id=username, message_ids=[int(id)])
            print(msg)
        except Exception as e:
            print(e)
            await c.stop()
            return False
        if msg[0].reply_markup:
            await asyncio.sleep(time)
            try:
                await c.join_chat(username)
            except:
                pass
            button = msg[0].reply_markup.inline_keyboard[0]
            results = []
            for btn in button:
                results.append(str(btn.text))
            for i in results:
                if text in i:
                    result = await msg[0].click(i)
            if result:
                db.set(f'isvote_{session[:15]}_{link}', True)
                await c.stop()
                return True
            else:
                db.set(f'isvote_{session[:15]}_{link}', True)
                await c.stop()
                return True
        else:
            await c.stop()
            return False
    else:
        await c.stop()
        return False