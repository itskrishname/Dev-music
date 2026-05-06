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

import httpx
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app


TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"
_WAIFU_APIS = [
    "https://api.waifu.pics/sfw/waifu",
    "https://api.waifu.im/search/?included_tags=waifu&is_nsfw=false",
]


@app.on_message(filters.command("waifu") & ~BANNED_USERS)
async def TeamDev_waifu(_, message: Message):
    url = None
    async with httpx.AsyncClient(timeout=12.0) as client:
        for api in _WAIFU_APIS:
            try:
                resp = await client.get(api)
                if resp.status_code == 200:
                    data = resp.json()
                    url = data.get("url") or (data.get("images") or [{}])[0].get("url")
                    if url:
                        break
            except Exception as e:
                print(f"[Waifu API {api}] {e}")
                continue

    if url:
        await message.reply_photo(
            photo=url,
            caption=(
                f"» Here's your waifu~\n\n"
                f"Request by {message.from_user.mention}\n"
                f"Powered by @Team_X_Og"
            ),
        )
    else:
        await message.reply_text("» Couldn't fetch a waifu image right now. Try again!")
