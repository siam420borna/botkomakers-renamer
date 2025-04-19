
from pyrogram import Client, filters
from helper.database import ban_user, remove_ban, total_user
from config import ADMIN
from pyrogram.types import Message

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("ban"))
async def ban(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("⚠️ ব্যবহার: `/ban user_id`", quote=True)
    try:
        user_id = int(message.command[1])
        ban_user(user_id)
        await message.reply(f"✅ `{user_id}` কে ব্যান করা হয়েছে!", quote=True)
    except Exception as e:
        await message.reply(f"❌ ভুল হয়েছে: {e}", quote=True)

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("unban"))
async def unban(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("⚠️ ব্যবহার: `/unban user_id`", quote=True)
    try:
        user_id = int(message.command[1])
        remove_ban(user_id)
        await message.reply(f"✅ `{user_id}` কে আনব্যান করা হয়েছে!", quote=True)
    except Exception as e:
        await message.reply(f"❌ ভুল হয়েছে: {e}", quote=True)

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("users"))
async def users(client, message: Message):
    count = total_user()
    await message.reply(f"👥 মোট ইউজার: **{count}**", quote=True)
