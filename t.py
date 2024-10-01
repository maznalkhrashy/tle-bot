from telethon.sync import TelegramClient, events

api_id = 29848011
api_hash = 'ab9bd73716cfe9939ea5ff0bd9bad498'

with TelegramClient('session', api_id, api_hash) as client:
    @client.on(events.NewMessage(pattern='/start'))
    async def start_handler(event):
        chat_id = event.chat_id
        await client.send_message(chat_id, 'مرحبًا بك! تم تشغيل البوت بنجاح.')

    client.run_until_disconnected()