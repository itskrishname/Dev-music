"""
                      [TeamDev](https://t.me/team_x_og)
          
          Project Id -> 39.
          Project Name -> TeamDev X Music
          Project Age -> 15D+ (Updated On 05/05/2026)
          Project Idea By -> @MR_ARMAN_08
          Project Dev -> @MR_ARMAN_08
          Powered By -> @Team_X_Og ( On Telegram )
          Updates -> @TeamDevXBots ( On telegram )
    
    Setup Guides -> Read > README.md
    
          This Script Part Off https://t.me/Team_X_Og's Team.
          Copyright ©️ 2026 TeamDev | @Team_X_Og
          
    • Some Quick Help
    - Read Full README.md For Understanding The Content.
    - If You Need Any Help Contact Us In @Team_X_Og's Group
    
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
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from config import BANNED_USERS
from strings import get_command
from TeamDevXMusic import app
from TeamDevXMusic.toolkit.datastore import (
    autoplay_off,
    autoplay_on,
    get_lang,
    is_autoplay_on,
)
from TeamDevXMusic.toolkit.guards.language import language


TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"


def TeamDev_autoplay_keyboard(enabled: bool, _) -> InlineKeyboardMarkup:
    status_btn = (
        InlineKeyboardButton("Eɴᴀʙʟᴇᴅ (Tᴀᴘ Tᴏ Dɪsᴀʙʟᴇ)", callback_data="autoplay_toggle_off")
        if enabled
        else InlineKeyboardButton("Dɪsᴀʙʟᴇᴅ (Tᴀᴘ Tᴏ Eɴᴀʙʟᴇ)", callback_data="autoplay_toggle_on")
    )
    return InlineKeyboardMarkup([
        [status_btn],
        [InlineKeyboardButton("Close", callback_data="close")],
    ])


def mr_d_status_text(enabled: bool) -> str:
    if enabled:
        return (
            "**AutoPlay** is currently **ON**\n\n"
            "Wʜᴇɴ ᴛʜᴇ ϙᴜᴇᴜᴇ ᴇɴᴅs, I'ʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ғɪɴᴅ ᴀɴᴅ ᴘʟᴀʏ\n"
            "ᴀ ʀᴇʟᴀᴛᴇᴅ YᴏᴜTᴜʙᴇ ᴛʀᴀᴄᴋ — ɴᴏ ɪɴᴛᴇʀʀᴜᴘᴛɪᴏɴs!\n\n"
            "💡 Turn off if you only want to play requested songs."
        )
    else:
        return (
            "**AutoPlay** is currently **OFF**\n\n"
            "Wʜᴇɴ ᴛʜᴇ ϙᴜᴇᴜᴇ ᴇɴᴅs, ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ sᴛᴏᴘ ᴘʟᴀʏɪɴɢ.\n\n"
            "💡 Turn on to keep the music going automatically!"
        )


@app.on_message(filters.command(["autoplay", "ap"]) & filters.group & ~BANNED_USERS)
@language
async def team_x_og_autoplay_command(_, message: Message, __):
    chat_id = message.chat.id
    args = message.command[1].lower() if len(message.command) > 1 else None

    enabled = await is_autoplay_on(chat_id)

    if args == "on":
        if enabled:
            return await message.reply_text(
                "✅ **AutoPlay** is already **ON** for this group!"
            )
        await autoplay_on(chat_id)
        return await message.reply_text(
            "**AutoPlay turned ON!**\n\n"
            "I'ʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴘʟᴀʏ ʀᴇʟᴀᴛᴇᴅ YᴏᴜTᴜʙᴇ sᴏɴɢs ᴡʜᴇɴ ᴛʜᴇ ϙᴜᴇᴜᴇ ᴇɴᴅs.\n\n"
            "Powered by @Team_X_Og"
        )
    elif args == "off":
        if not enabled:
            return await message.reply_text(
                "**AutoPlay** is already **OFF** for this group!"
            )
        await autoplay_off(chat_id)
        return await message.reply_text(
            "**AutoPlay turned OFF!**\n\n"
            "Bᴏᴛ ᴡɪʟʟ sᴛᴏᴘ ᴘʟᴀʏɪɴɢ ᴡʜᴇɴ ᴛʜᴇ ϙᴜᴇᴜᴇ ᴇɴᴅs.\n\n"
            "Powered by @Team_X_Og"
        )

    keyboard = TeamDev_autoplay_keyboard(enabled, __)
    await message.reply_text(
        mr_d_status_text(enabled),
        reply_markup=keyboard,
    )


@app.on_callback_query(filters.regex("^autoplay_toggle_(on|off)$") & ~BANNED_USERS)
async def TeamDev_autoplay_callback(_, query: CallbackQuery):
    chat_id = query.message.chat.id
    action = query.data.split("_")[-1]

    try:
        member = await _.get_chat_member(chat_id, query.from_user.id)
        from pyrogram import enums
        if member.status not in (
            enums.ChatMemberStatus.ADMINISTRATOR,
            enums.ChatMemberStatus.OWNER,
        ):
            return await query.answer(
                "⚠️ Only admins can toggle AutoPlay!", show_alert=True
            )
    except Exception:
        return await query.answer("⚠️ Could not verify permissions.", show_alert=True)

    if action == "on":
        await autoplay_on(chat_id)
        enabled = True
        await query.answer("AutoPlay enabled!", show_alert=False)
    else:
        await autoplay_off(chat_id)
        enabled = False
        await query.answer("AutoPlay disabled!", show_alert=False)

    language = await get_lang(chat_id)
    from strings import get_string
    _ = get_string(language)

    keyboard = TeamDev_autoplay_keyboard(enabled, _)
    try:
        await query.message.edit_text(
            mr_d_status_text(enabled),
            reply_markup=keyboard,
        )
    except Exception:
        pass
