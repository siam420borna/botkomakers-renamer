
from pyrogram import Client, filters
from pyrogram.types import Message
from helper.database import set_caption, get_caption, delete_caption

@Client.on_message(filters.command("set_caption"))
async def set_user_caption(bot, message: Message):
    if len(message.text.split(" ", 1)) < 2:
        return await message.reply("**দয়া করে ক্যাপশন দিন। উদাহরণ:**
`/set_caption 📁 File: {filename}\n📦 Size: {filesize}`")
    caption = message.text.split(" ", 1)[1]
    set_caption(message.from_user.id, caption)
    await message.reply("✅ আপনার ক্যাপশন সেট করা হয়েছে।")

@Client.on_message(filters.command("see_caption"))
async def see_user_caption(bot, message: Message):
    caption = get_caption(message.from_user.id)
    if caption:
        await message.reply(f"**আপনার বর্তমান ক্যাপশন:**

`{caption}`")
    else:
        await message.reply("❌ আপনি এখনো কোনো ক্যাপশন সেট করেননি।")

@Client.on_message(filters.command("del_caption"))
async def delete_user_caption(bot, message: Message):
    delete_caption(message.from_user.id)
    await message.reply("🗑️ আপনার ক্যাপশন ডিলিট করা হয়েছে।")
