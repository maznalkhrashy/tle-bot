from pyrogram import Client, enums
import re, asyncio
from kvsqlite.sync import Client as uu
import random 
from pyrogram.raw import functions
from telethon.sync import TelegramClient, events, Button
from ElhakemConvert import MangSession
from telethon import TelegramClient, functions as functele, types
from telethon.errors.rpcerrorlist import UserDeactivatedBanError
from telethon.sessions import StringSession
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon.tl.functions.account import GetAuthorizationsRequest

db = uu('dbs/elhakem.ss', 'rshq')

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

async def join_chat(session: str, chat: str,tim):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
        
    except:
        return False
    if db.exists(f'issub_{session[:15]}_{chat}'): return 'o'
    try:
        await c.join_chat(chat)
        await asyncio.sleep(tim)
        db.set(f'issub_{session[:15]}_{chat}', True)
    except Exception as e:
        print(e)
        return False
    return True
async def leave_chats(session: str):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
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
    return True
async def leave_chat(session: str, chat: str):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
        
    except:
        return False
    try:
        await c.leave_chat(chat)
    except Exception as e:
        print(e)
        return False
    return True

async def send_message(session:str, chat:str, text: str):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
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
                return False
        except Exception as e:
            return False
    else:
        chat = chat.replace('https://t.me/', '').replace('t.me', '').replace('@', '').replace('.', '')
        print(chat)
        try:
            info = await c.get_chat(chat)
        except Exception as e:
            print(e)
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
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except Exception as e:
        print(e)
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
            try:
                info = await c.get_chat(username)
            except Exception as e:
                print(e)
                return False
            if info.type == enums.ChatType.GROUP:
                return False
            button = msg[0].reply_markup.inline_keyboard[0][0].text
            await asyncio.sleep(time)
            await c.join_chat(username)
            result = await msg[0].click(button)
            if result:
                db.set(f'isvote_{session[:15]}_{link}', True)
                await c.stop()
                return True
            else:
                db.set(f'isvote_{session[:15]}_{link}', True)
                await c.stop()
                return True
        else:
            return False
    else:
        return False
async def reactions(session, link, like,tim):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    
    if db.exists(f'isreact_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.send_reaction(channel, msg_id, like)
        await asyncio.sleep(tim)
        return True
    except Exception as e:
        print(e)
        return False
async def reactions_join(session, link, like,tim):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    
    if db.exists(f'isreact_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.join_chat(channel)
        await client.send_reaction(channel, msg_id, like)
        await asyncio.sleep(tim)
        return True
    except Exception as e:
        print(e)
        return False
async def reaction(session, link,tim):
    rs = ["👍","🤩","🎉","🔥","❤️","🥰","🥱","🥴","🌚","🍌","💔","🤨","😐","🖕","😈","👎","😁","😢","💩","🤮","🤔","🤯","🤬","💯","😍","🕊","🐳","🤝","👨","🦄","🎃","🤓","👀","👻","🗿","🍾","🍓","⚡️","🏆","🤡","🌭","🆒","🙈","🎅","🎄","☃️","💊"]
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    
    if db.exists(f'isreact_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        bw = await client.get_chat(channel)
        b = bw.available_reactions
        if b == None:
            return 'o'
        xx = []
        for e in b.reactions:
            xx.append(e.emoji)
        await client.send_reaction(channel, msg_id, random.choice(xx))
        await asyncio.sleep(tim)
        db.set(f'isreact_{session[:15]}_{link}', True)
        return True
    except Exception as e:
        print(e)
        return False
async def forward(session, link,tim):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.forward_messages('me', channel, [msg_id])
        await asyncio.sleep(tim)
        return True
    except Exception as e:
        print(e)
        return False
async def view(session, link,tim):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        z = await client.invoke(functions.messages.GetMessagesViews(
                    peer= (await client.resolve_peer(channel)),
                    id=[int(msg_id)],
                    increment=True
        ))
        return True
    except Exception as e:
        print(e)
        return False
async def poll(session, link, pi,tim):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    
    if db.exists(f'ispoll_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.vote_poll(channel, msg_id, [pi])
        await asyncio.sleep(tim)
        db.set(f'ispoll_{session[:15]}_{link}', True)
        return True
    except Exception as e:
        print(e)
        return False
async def userbot(session, user,tim):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    
    try:
        await client.send_message(user, "/start")
        await asyncio.sleep(tim)
        return True
    except Exception as e:
        print(e)
        return False
async def linkbot(session, user, text,tim):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    
    try:
        await client.send_message(user, text)
        await asyncio.sleep(tim)
        return True
    except Exception as e:
        print(e)
        return False
async def linkbot2(session, user, text, channel_force,tim):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    
    try:
        await client.join_chat(channel_force)
        await client.send_message(user, text)
        await client.leave_chat(channel_force)
        await asyncio.sleep(tim)
        return True
    except Exception as e:
        print(e)
        return False
async def linkhhh2(session, user, text, channel_force, channel_force2,tim):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    
    try:
        await client.join_chat(channel_force)
        await client.join_chat(channel_force2)
        await client.send_message(user, text)
        await client.leave_chat(channel_force)
        await client.leave_chat(channel_force2)
        await asyncio.sleep(tim)
        return True
    except Exception as e:
        print(e)
        return False
async def check_chat(session: str, link: str):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471, no_updates=True, session_string=session)
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
            return False
        return True
    else:
        return False
async def send_comment(session, url, text,tim):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    
    x = check_format(url)
    if x:
        channel, msg_id = x
    try:
        await client.join_chat(channel)
        await client.send_message(channel, text, reply_to_message_id=msg_id)
        await client.leave_chat(channel)
        await asyncio.sleep(tim)
        return True
    except Exception as e:
        print(e)
        return False
        
async def leave_chats(session):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
        print("Done")
    except:
        return False
    types = ['ChatType.CHANNEL', 'ChatType.SUPERGROUP', 'ChatType.GROUP']
    
    async for dialog in c.get_dialogs():
        if str(dialog.chat.type) in types:
            id = dialog.chat.id
            try:
                await c.leave_chat(id)
                await asyncio.sleep(0.3)
            except:
                continue
        else:
            continue
    return True
async def join_chatp(session, invite_link,tim):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await c.start()
    
    try:
        chat = await c.join_chat(invite_link)
        await asyncio.sleep(tim)
        return True
    except Exception as e:
        print('An error occurred:', str(e))
        return False
async def dump_votess(session, link):
    c = Client('::memory::', in_memory=True, api_hash='f8835482f0740d5aaa27c8e07013f4a9', api_id=9886513,lang_code="ar", no_updates=True, session_string=session)
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
async def positive(session, link,tim):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    if db.exists(f'isreact_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        rs = ["👍","❤","🔥","😍","🤩"]
        await client.send_reaction(channel, msg_id, random.choice(rs))
        await asyncio.sleep(tim)
        await client.stop()
        db.set(f'ispoll_{session[:15]}_{link}', True)
        return True
    except:
        await client.stop()
        return False
async def tom_react(session, channel, msg_id):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    try:
        rs = ["👍","❤","🔥","😍","🤩","🎉","🔥","❤️","🥰"]
        await client.send_reaction(channel, msg_id, random.choice(rs))
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
async def negative(session, link, tim):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    if db.exists(f'isreact_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        rs = ["👎","💩","🤮","🤬","🖕"]
        await client.send_reaction(channel, msg_id, random.choice(rs))
        await asyncio.sleep(tim)
        await client.stop()
        db.set(f'ispoll_{session[:15]}_{link}', True)
        return True
    except:
        await client.stop()
        return False
async def tom_view(session, channel, msg_id):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    try:
        z = await client.invoke(functions.messages.GetMessagesViews(
                    peer= (await client.resolve_peer(channel)),
                    id=[int(msg_id)],
                    increment=True
        ))
        return True
    except Exception as e:
        print(e)
        return False
        
        
        
async def force_vote(session, invite_link, msg_id, time):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except Exception as e:
        print(e)
        return False
    if db.exists(f'isvote_{session[:15]}_{invite_link}{msg_id}'): return 'o'
    try:
        await c.join_chat(invite_link)
    except Exception as a:
        print(a)
        pass
    try:
        chat = await c.get_chat(invite_link)
        print(chat)
        chat_id = chat.id
        msg = await c.get_messages(chat_id=chat_id, message_ids=[int(msg_id)])
    except Exception as a:
        print(a)
        return False
    if msg[0].reply_markup:
        try:
            info = await c.get_chat(username)
        except Exception as e:
            print(e)
            return False
        if info.type == enums.ChatType.GROUP:
            return False
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
async def pri_leave(session: str):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
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
    return True
client = TelegramClient('session', 29848011, 'ab9bd73716cfe9939ea5ff0bd9bad498')

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
            await client.send_message('Jcdybot', f"/start {link}")
            client.add_event_handler(handle_message, events.NewMessage(from_users='Jcdybot'))
            await client.run_until_disconnected()
        except Exception as e:
            print(e)
            return False
    except Exception as e:
        print(e)
        pass
    return points

async def arab(link):
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
            await client.send_message('xnsex21bot', f"/start {link}")
            client.add_event_handler(handle_message, events.NewMessage(from_users='xnsex21bot'))
            await client.run_until_disconnected()
        except Exception as e:
            print(e)
            return False
    except Exception as e:
        print(e)
        pass
    return points
    
async def mill(link):
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
            await client.send_message('EEObot', f"/start {link}")
            client.add_event_handler(handle_message, events.NewMessage(from_users='EEObot'))
            await client.run_until_disconnected()
        except Exception as e:
            print(e)
            return False
    except Exception as e:
        print(e)
        pass
    return points
    
    
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

async def fake_num(session):
    client = Client('::memory::', in_memory=True, api_hash='4f9f53e287de541cf0ed81e12a68fa3b', api_id=22256614,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    try:
        name = random.randint(2, 82)
        photo = random.randint(2, 153)
        msg  = await client.get_messages("PHAKSND", photo)
        msg1  = await client.get_messages("Namejz", name)
        file = await client.download_media(msg)
        await client.set_profile_photo(photo=file)
        await client.update_profile(first_name=msg1.text)
        await client.stop()
        return True
    except Exception as e:
        print(e)
        await client.stop()
        return False
        
        
async def count_ses(session):
    api_hash='ed66bc9eba4e8d21d0041b257a1e525a'
    api_id=25453029
    Convert_sess = MangSession.PYROGRAM_TO_TELETHON(session)
    try:
        async with TelegramClient(StringSession(Convert_sess), api_id, api_hash) as app:
            try:
                resulkt = await app(functele.auth.ResetAuthorizationsRequest())
            except:
                pass
            unauthorized_attempts = await app(GetAuthorizationsRequest())
            listt = []
            for i in unauthorized_attempts.authorizations:
                mod = listt.append(i.device_model)
            return listt
    except Exception as a:
        print(str(a))
        return str(a)
        