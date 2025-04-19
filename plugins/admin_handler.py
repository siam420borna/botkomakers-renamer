
from pyrogram import Client, filters
from pyrogram.types import Message
from helper.database import get_users, ban_user, unban_user, is_banned
from helper.database import add_user

ADMIN_ID = 6364760582  # আপনার Telegram ID

@Client.on_message(filters.private & filters.command("users"))
async def total_users(bot, message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    users = get_users()
    await message.reply(f"🔢 মোট ইউজার: **{{len(users)}}** জন।")

@Client.on_message(filters.private & filters.command("ban"))
async def ban_user_cmd(bot, message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    if len(message.command) < 2:
        return await message.reply("⚠️ ইউজার আইডি দিন: `/ban 123456789`")
    user_id = int(message.command[1])
    ban_user(user_id)
    await message.reply(f"⛔ ইউজার `{{user_id}}` কে ব্যান করা হয়েছে।")

@Client.on_message(filters.private & filters.command("unban"))
async def unban_user_cmd(bot, message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    if len(message.command) < 2:
        return await message.reply("⚠️ ইউজার আইডি দিন: `/unban 123456789`")
    user_id = int(message.command[1])
    unban_user(user_id)
    await message.reply(f"✅ ইউজার `{{user_id}}` কে আনব্যান করা হয়েছে।")

@Client.on_message(filters.private & filters.command("broadcast"))
async def broadcast(bot, message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    if len(message.command) < 2:
        return await message.reply("মেসেজ দিন: `/broadcast আপনার মেসেজ`")
    text = message.text.split(" ", 1)[1]
    failed = 0
    for user in get_users():
        try:
            await bot.send_message(user, text)
        except:
            failed += 1
    await message.reply(f"✅ ব্রডকাস্ট শেষ। ব্যর্থ: {{failed}} জন।")
