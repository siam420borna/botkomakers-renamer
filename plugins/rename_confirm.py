
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

@Client.on_message(filters.document | filters.video | filters.audio)
async def incoming_media(client, message: Message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ হ্যাঁ", callback_data="confirm_rename"),
         InlineKeyboardButton("❌ না", callback_data="cancel_rename")]
    ])
    await message.reply_text("আপনি কি ফাইলটি রিনেম করতে চান?", reply_markup=buttons)

@Client.on_callback_query(filters.regex("confirm_rename"))
async def confirm_rename(client, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("নিচে নতুন নাম দিন (এক্সটেনশন সহ):")

@Client.on_callback_query(filters.regex("cancel_rename"))
async def cancel_rename(client, callback_query: CallbackQuery):
    await callback_query.answer("রিনেম বাতিল করা হয়েছে!", show_alert=True)
    await callback_query.message.delete()
