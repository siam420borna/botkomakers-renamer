
import time
from pyrogram import Client, filters
from pyrogram.types import Message
from helper.utils import progress_for_pyrogram

@Client.on_message(filters.command("rename") & filters.reply)
async def rename_file(client, message: Message):
    if not message.reply_to_message.document and not message.reply_to_message.video and not message.reply_to_message.audio:
        return await message.reply("⚠️ অনুগ্রহ করে একটি ফাইল রিপ্লাই করে কমান্ড দিন।")

    sent = await message.reply("⏬ ফাইল ডাউনলোড শুরু হচ্ছে...")
    start_time = time.time()
    
    try:
        file_path = await client.download_media(
            message.reply_to_message,
            progress=progress_for_pyrogram,
            progress_args=("⬇️ ডাউনলোড হচ্ছে...", sent, start_time)
        )
        download_time = round(time.time() - start_time, 2)
    except Exception as e:
        return await sent.edit(f"❌ ডাউনলোডে সমস্যা: `{e}`")

    await sent.edit("✅ ডাউনলোড শেষ! ⏫ আপলোড শুরু হচ্ছে...")
    upload_start = time.time()

    try:
        await message.reply_document(
            file_path,
            caption="✅ রিনেম সফল!",
            progress=progress_for_pyrogram,
            progress_args=("⬆️ আপলোড হচ্ছে...", sent, upload_start)
        )
        upload_time = round(time.time() - upload_start, 2)
        await sent.edit(f"✅ কাজ শেষ!
⏬ ডাউনলোড সময়: {download_time} সেকেন্ড
⏫ আপলোড সময়: {upload_time} সেকেন্ড")
    except Exception as e:
        await sent.edit(f"❌ আপলোডে সমস্যা: `{e}`")
