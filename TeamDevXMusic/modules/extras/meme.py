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

import requests
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app

TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

@app.on_message(filters.command("meme") & ~BANNED_USERS)
async def TeamDev_meme_command(_, message: Message):
    args = message.text.split()
    category = args[1] if len(args) > 1 else ""
    api_url = f"https://meme-api.com/gimme/{category}" if category else "https://meme-api.com/gimme"

    try:
        response = requests.get(api_url, timeout=10)
        data = response.json()

        if response.status_code == 403 or ("message" in data and "Unable to Access" in data["message"]):
            return await message.reply_text(
                "» Memes from this category are not available. Please try another one."
            )

        meme_url = data.get("url")
        title = data.get("title", "Meme")

        bot_info = await app.get_me()
        caption = (
            f"**{title}**\n\n"
            f"» Request by {message.from_user.mention}\n"
            f"» @{bot_info.username} | **@{TEAM_X_OG}**"
        )

        await message.reply_photo(photo=meme_url, caption=caption)

    except Exception as e:
        print(f"[Meme Error] {e}")
        await message.reply_text("» Sorry, couldn't fetch a meme right now. Try again.")
