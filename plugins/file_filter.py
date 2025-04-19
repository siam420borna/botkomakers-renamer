
from pyrogram import Client, filters
from pyrogram.types import Message

MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024  # 2GB

@Client.on_message(filters.document | filters.video | filters.audio)
async def validate_file(client, message: Message):
    file = message.document or message.video or message.audio
    if file.file_size > MAX_FILE_SIZE:
        return await message.reply("❌ দুঃখিত! 2GB এর বেশি ফাইল রিনেম করা যাবে না।")
    
    # Supported MIME types check (optional, can be expanded)
    allowed_types = ["application", "video", "audio"]
    if not any(file.mime_type.startswith(t) for t in allowed_types):
        return await message.reply("❌ এই ধরনের ফাইল সাপোর্ট করে না।")

    # If valid, pass to rename_confirm
    from plugins.rename_confirm import incoming_media
    await incoming_media(client, message)
