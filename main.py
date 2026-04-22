from telethon import TelegramClient, events
import os

api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")

# Persistent disk mount path
session_path = "/var/data/kemal_session"

client = TelegramClient(session_path, api_id, api_hash)

SOURCE_CHAT = -1003485696251
TARGET_CHAT = -1003824688558

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def handler(event):
    text = event.raw_text or ""

    if not text.strip():
        return

    await client.send_message(TARGET_CHAT, text)

    print("Kopyalandı:")
    print(text)
    print("-----")

async def main():
    print("Bot çalışıyor... Kaynak gruptaki tüm metin mesajları hedef gruba kopyalanacak.")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()