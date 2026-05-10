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

import asyncio

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait, MessageDeleteForbidden, RPCError
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app
from TeamDevXMusic.modules.extras.admin_utils import admin_filter


TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"


def TeamDev_chunk_list(lst: list, n: int = 100):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


@app.on_message(filters.command("purge") & admin_filter & ~BANNED_USERS)
async def mr_d_purge(client, message: Message):
    if message.chat.type != ChatType.SUPERGROUP:
        return await message.reply("**ɪ ᴄᴀɴ'ᴛ ᴘᴜʀɢᴇ ɪɴ ᴀ ʙᴀsɪᴄ ɢʀᴏᴜᴘ. ᴄᴏɴᴠᴇʀᴛ ɪᴛ ᴛᴏ ᴀ sᴜᴘᴇʀɢʀᴏᴜᴘ.**")
    if not message.reply_to_message:
        return await message.reply("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴛᴀʀᴛ ᴘᴜʀɢᴇ!**")

    ids = list(range(message.reply_to_message.id, message.id))
    try:
        for chunk in TeamDev_chunk_list(ids):
            try:
                await client.delete_messages(chat_id=message.chat.id, message_ids=chunk, revoke=True)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.value)
        await message.delete()
        confirm = await message.reply(f"» | **ᴅᴇʟᴇᴛᴇᴅ `{len(ids)}` ᴍᴇssᴀɢᴇs.**")
        await asyncio.sleep(3)
        await confirm.delete()
    except MessageDeleteForbidden:
        await message.reply("**ɪ ᴄᴀɴ'ᴛ ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs. ᴍᴀʏ ʙᴇ ᴛᴏᴏ ᴏʟᴅ ᴏʀ ɴᴏ ʀɪɢʜᴛs.**")
    except RPCError as e:
        await message.reply(f"**ᴇʀʀᴏʀ:**\n<code>{e}</code>")


@app.on_message(filters.command("spurge") & admin_filter & ~BANNED_USERS)
async def team_x_og_spurge(client, message: Message):
    """Silent purge — deletes without confirmation message."""
    if message.chat.type != ChatType.SUPERGROUP:
        return await message.reply("**ɪ ᴄᴀɴ'ᴛ ᴘᴜʀɢᴇ ɪɴ ᴀ ʙᴀsɪᴄ ɢʀᴏᴜᴘ.**")
    if not message.reply_to_message:
        return await message.reply("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴛᴀʀᴛ ᴘᴜʀɢᴇ!**")

    ids = list(range(message.reply_to_message.id, message.id))
    try:
        for chunk in TeamDev_chunk_list(ids):
            try:
                await client.delete_messages(chat_id=message.chat.id, message_ids=chunk, revoke=True)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.value)
        await message.delete()
    except MessageDeleteForbidden:
        await message.reply("**ɪ ᴄᴀɴ'ᴛ ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs.**")
    except RPCError as e:
        await message.reply(f"**ᴇʀʀᴏʀ:**\n<code>{e}</code>")


@app.on_message(filters.command("del") & admin_filter & ~BANNED_USERS)
async def TeamDev_del_msg(client, message: Message):
    if message.chat.type != ChatType.SUPERGROUP:
        return await message.reply("**ɪ ᴄᴀɴ'ᴛ ᴘᴜʀɢᴇ ɪɴ ᴀ ʙᴀsɪᴄ ɢʀᴏᴜᴘ.**")
    if not message.reply_to_message:
        return await message.reply("**ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ?**")
    try:
        await message.delete()
        await client.delete_messages(
            chat_id=message.chat.id, message_ids=message.reply_to_message.id
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception as e:
        await message.reply(f"**ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ:**\n<code>{e}</code>")
