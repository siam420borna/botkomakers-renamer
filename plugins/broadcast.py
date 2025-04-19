
from pyrogram import Client, filters
from pyrogram.types import Message
from helper.database import get_users
from config import ADMIN

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("broadcast"))
async def broadcast_handler(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("🔰 ব্যবহার: `/broadcast আপনার মেসেজ`", quote=True)
    
    text = message.text.split(" ", 1)[1]
    users = get_users()
    sent_count = 0
    fail_count = 0

    await message.reply(f"📢 ব্রডকাস্ট শুরু হয়েছে! মোট ইউজার: {len(users)}")

    for user_id in users:
        try:
            await client.send_message(user_id, text)
            sent_count += 1
        except:
            fail_count += 1

    await message.reply(f"✅ ব্রডকাস্ট শেষ!

✅ পাঠানো হয়েছে: {sent_count}
❌ ফেল হয়েছে: {fail_count}")
