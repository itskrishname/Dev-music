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

from config import BANNED_USERS
from strings import get_command
from TeamDevXMusic import YouTube, app
from TeamDevXMusic.relay.caller import TeamDevXMusic
from TeamDevXMusic.helpers import db
from TeamDevXMusic.toolkit import AdminRightsCheck, seconds_to_min

SEEK_COMMAND = get_command("SEEK_COMMAND")


@app.on_message(filters.command(SEEK_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def seek_comm(cli, message: Message, _, chat_id):
    if len(message.command) == 1:
        return await message.reply_text(_["admin_28"])
    query = message.text.split(None, 1)[1].strip()
    if not query.isnumeric():
        return await message.reply_text(_["admin_29"])
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text(_["queue_2"])
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text(_["admin_30"])
    file_path = playing[0]["file"]
    if "index_" in file_path or "live_" in file_path:
        return await message.reply_text(_["admin_30"])
    duration_played = int(playing[0]["played"])
    duration_to_skip = int(query)
    duration = playing[0]["dur"]
    if message.command[0][-2] == "c":
        if (duration_played - duration_to_skip) <= 10:
            return await message.reply_text(
                _["admin_31"].format(seconds_to_min(duration_played), duration)
            )
        to_seek = duration_played - duration_to_skip + 1
    elif (duration_seconds - (duration_played + duration_to_skip)) <= 10:
        return await message.reply_text(
            _["admin_31"].format(seconds_to_min(duration_played), duration)
        )
    else:
        to_seek = duration_played + duration_to_skip + 1
    mystic = await message.reply_text(_["admin_32"])
    if "vid_" in file_path:
        n, file_path = await YouTube.video(playing[0]["vidid"], True)
        if n == 0:
            return await message.reply_text(_["admin_30"])
    try:
        await TeamDevXMusic.seek_stream(
            chat_id,
            file_path,
            seconds_to_min(to_seek),
            duration,
            playing[0]["streamtype"],
        )
    except Exception:
        return await mystic.edit_text(_["admin_34"])
    if message.command[0][-2] == "c":
        db[chat_id][0]["played"] -= duration_to_skip
    else:
        db[chat_id][0]["played"] += duration_to_skip
    await mystic.edit_text(_["admin_33"].format(seconds_to_min(to_seek)))
