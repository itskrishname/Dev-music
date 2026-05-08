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
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app

TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

def TeamDev_fetch_pypi(package_name: str) -> dict | None:
    try:
        resp = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"[PyPI Error] {e}")
        return None


@app.on_message(filters.command("pypi") & ~BANNED_USERS)
async def mr_d_pypi_command(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "**» Please provide a Python package name.**\n\nExample: `/pypi requests`",
            parse_mode=ParseMode.MARKDOWN,
        )

    package_name = message.command[1]
    pypi_data = TeamDev_fetch_pypi(package_name)

    if pypi_data:
        info = pypi_data["info"]
        project_url = (
            (info.get("project_urls") or {}).get("Homepage")
            or info.get("home_page")
            or "N/A"
        )
        text = (
            f"» **Package:** `{info['name']}`\n"
            f"» **Version:** `{info['version']}`\n"
            f"» **Description:** {info.get('summary') or 'No description.'}\n"
            f"» **URL:** [Click here]({project_url})\n\n"
            f"_Powered by @SECRECT_BOT_UPDATES"
        )
        await message.reply_text(text, parse_mode=ParseMode.MARKDOWN)
    else:
        await message.reply_text(
            "**» Package not found.**\n"
            "Check the spelling or try another package name.",
            parse_mode=ParseMode.MARKDOWN,
        )
