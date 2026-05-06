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
from pyrogram.types import Message
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from strings import get_command
from TeamDevXMusic import app
from TeamDevXMusic.relay.caller import TeamDevXMusic
from TeamDevXMusic.toolkit.guards.play import PlayWrapper
from TeamDevXMusic.toolkit.logutil import play_logs
from TeamDevXMusic.toolkit.engine.streamer import stream

STREAM_COMMAND = get_command("STREAM_COMMAND")


@app.on_message(filters.command(STREAM_COMMAND) & filters.group & ~BANNED_USERS)
@PlayWrapper
async def stream_command(
    client,
    message: Message,
    _,
    chat_id,
    video,
    channel,
    playmode,
    url,
    fplay,
):
    if url:
        mystic = await message.reply_text(
            _["play_2"].format(channel) if channel else _["play_1"]
        )
        try:
            await TeamDevXMusic.stream_call(url)
        except NoActiveGroupCall:
            await mystic.edit_text(
                "ᴛʜᴇʀᴇ's ᴀɴ ɪssᴜᴇ ᴡɪᴛʜ ᴛʜᴇ ʙᴏᴛ. ᴘʟᴇᴀsᴇ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ ᴀɴᴅ ᴀsᴋ ᴛʜᴇᴍ ᴛᴏ ᴄʜᴇᴄᴋ ʟᴏɢɢᴇʀ ɢʀᴏᴜᴘ."
            )
            return await app.send_message(
                config.LOG_GROUP_ID,
                "ᴘʟᴇᴀsᴇ ᴛᴜʀɴ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.. ʙᴏᴛ ɪs ɴᴏᴛ ᴀʙʟᴇ ᴛᴏ sᴛʀᴇᴀᴍ ᴜʀʟs..",
            )
        except Exception as e:
            return await mystic.edit_text(_["general_3"].format(type(e).__name__))
        await mystic.edit_text(_["str_2"])
        try:
            await stream(
                _,
                mystic,
                message.from_user.id,
                url,
                chat_id,
                message.from_user.first_name,
                message.chat.id,
                video=True,
                streamtype="index",
            )
        except Exception as e:
            ex_type = type(e).__name__
            err = e if ex_type == "AssistantErr" else _["general_3"].format(ex_type)
            return await mystic.edit_text(err)
        return await play_logs(message, streamtype="M3u8 or Index Link")
    else:
        await message.reply_text(_["str_1"])
