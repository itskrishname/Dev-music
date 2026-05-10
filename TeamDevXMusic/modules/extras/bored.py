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

import httpx
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app

TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

_BORED_API = "https://apis.scrimba.com/bored/api/activity"


@app.on_message(filters.command("bored") & ~BANNED_USERS)
async def mr_d_bored_command(_, message: Message):
    try:
        async with httpx.AsyncClient(timeout=10.0) as http:
            resp = await http.get(_BORED_API)

        if resp.status_code != 200:
            return await message.reply_text("» Failed to fetch an activity. Try again later.")

        activity = resp.json().get("activity")
        if activity:
            await message.reply_text(
                f"» **Feeling bored?**\n\n» **Try this:** `{activity}`\n\nPowered by @SECRECT_BOT_UPDATES",
                parse_mode=ParseMode.MARKDOWN,
            )
        else:
            await message.reply_text("» No activity found.")

    except Exception as e:
        print(f"[Bored Error] {e}")
        await message.reply_text("» Something went wrong while fetching a boredom buster.")
