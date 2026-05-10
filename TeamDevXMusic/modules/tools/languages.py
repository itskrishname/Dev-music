"""
                      [TeamDev](https://t.me/team_x_og)
          
          Project Id -> 39.
          Project Name -> TeamDev X Music
          Project Age -> 15D+ (Updated On 05/05/2026)
          Project Idea By -> @MR_ARMAN_08
          Project Dev -> @MR_ARMAN_08
          Powered By -> @SECRECT_BOT_UPDATES ( On Telegram )
          Updates -> @TeamDevXBots ( On telegram )
    
    Setup Guides -> Read > README.md
    
          This Script Part Off https://t.me/Team_X_Og's Team.
          Copyright ©️ 2026 TeamDev | @SECRECT_BOT_UPDATES
          
    • Some Quick Help
    - Read Full README.md For Understanding The Content.
    - If You Need Any Help Contact Us In @SECRECT_BOT_UPDATES's Group
    
         Compatible In BotApi 9.5 Fully
         Build For BotApi 9.5
         We'll Keep Update This Repo If We Got 30+ Stars In One Month Of Release.
"""

# Copyright (C) 2025 by @MR_ARMAN_08 @ Github, < https://github.com/justfortestingnothibghere >
# All rights reserved. © TeamDevXMusic

"""
TeamDevXMusic is a Telegram Music Bot by @MR_ARMAN_08.
Copyright (c) 2026 ~ Present Team TeamDevXMusic <https://github.com/justfortestingnothibghere>

This program is "Ristiricted" software: Don't Modify, Redistribute Or Sell This Project Proving As Your Project
TeamDev Will Take Action If They Find Any unauthorised usages.
"""


from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import BANNED_USERS
from strings import get_command, get_string, languages_present
from TeamDevXMusic import app
from TeamDevXMusic.toolkit.datastore import get_lang, set_lang
from TeamDevXMusic.toolkit.guards import ActualAdminCB, language, languageCB

def lanuages_keyboard(_):
    buttons = [
        InlineKeyboardButton(text=languages_present[i], callback_data=f"languages:{i}")
        for i in languages_present
    ]
    keyboardx = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]

    keyboardx.append(
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"], callback_data="settingsback_helper"
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ]
    )
    return InlineKeyboardMarkup(keyboardx)


LANGUAGE_COMMAND = get_command("LANGUAGE_COMMAND")


@app.on_message(filters.command(LANGUAGE_COMMAND) & filters.group & ~BANNED_USERS)
@language
async def langs_command(client, message: Message, _):
    keyboard = lanuages_keyboard(_)
    await message.reply_text(
        _["setting_1"].format(message.chat.title, message.chat.id),
        reply_markup=keyboard,
    )


@app.on_callback_query(filters.regex("LG") & ~BANNED_USERS)
@languageCB
async def lanuagecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except Exception:
        pass
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)


@app.on_callback_query(filters.regex(r"languages:(.*?)") & ~BANNED_USERS)
@ActualAdminCB
async def language_markup(client, CallbackQuery, _):
    langauge = CallbackQuery.data.split(":")[1]
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer(
            "ʏᴏᴜ'ʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜsɪɴɢ sᴀᴍᴇ ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ.", show_alert=True
        )
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer(
            "sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ʏᴏᴜʀ ʟᴀɴɢᴜᴀɢᴇ.", show_alert=True
        )
    except Exception:
        return await CallbackQuery.answer(
            "ғᴀɪʟᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ʟᴀɴɢᴜᴀɢᴇ ᴏʀ ᴛʜᴇ ʟᴀɴɢᴜᴀɢᴇ ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ.",
            show_alert=True,
        )
    await set_lang(CallbackQuery.message.chat.id, langauge)
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)
