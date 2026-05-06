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
from TeamDevXMusic import app
from TeamDevXMusic.relay.caller import TeamDevXMusic
from TeamDevXMusic.toolkit.datastore import is_muted, mute_on
from TeamDevXMusic.toolkit.guards import AdminRightsCheck

MUTE_COMMAND = get_command("MUTE_COMMAND")


@app.on_message(filters.command(MUTE_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if len(message.command) != 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"], disable_web_page_preview=True)
    await mute_on(chat_id)
    await TeamDevXMusic.mute_stream(chat_id)
    await message.reply_text(
        _["admin_6"].format(message.from_user.mention), disable_web_page_preview=True
    )
