
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from helper.database import set_lang, get_lang

@Client.on_message(filters.command("settings"))
async def settings_menu(client, message: Message):
    lang = await get_lang(message.from_user.id)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("বাংলা", callback_data="lang_bn"),
         InlineKeyboardButton("English", callback_data="lang_en")]
    ])
    await message.reply("⚙️ ভাষা নির্বাচন করুন:", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("lang_"))
async def change_language(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    lang_code = callback_query.data.split("_")[1]
    await set_lang(user_id, lang_code)

    lang_name = "বাংলা" if lang_code == "bn" else "English"
    await callback_query.answer()
    await callback_query.message.edit_text(f"✅ ভাষা পরিবর্তন হয়েছে: {lang_name}")
