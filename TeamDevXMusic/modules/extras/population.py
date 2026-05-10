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

import requests
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app


TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

@app.on_message(filters.command("population") & ~BANNED_USERS)
async def TeamDev_population_command(_, message: Message):
    if len(message.text.split()) < 2:
        return await message.reply_text(
            "» Please provide a country code.\nExample: `/population IN`",
            parse_mode=ParseMode.MARKDOWN,
        )

    country_code = message.text.split(maxsplit=1)[1].strip().upper()
    api_url = f"https://restcountries.com/v3.1/alpha/{country_code}"

    try:
        resp = requests.get(api_url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        if data:
            country_name = data[0].get("name", {}).get("common", "N/A")
            capital = data[0].get("capital", ["N/A"])[0]
            population = data[0].get("population", "N/A")
            region = data[0].get("region", "N/A")
            subregion = data[0].get("subregion", "N/A")
            area = data[0].get("area", "N/A")

            text = (
                f"» **Country Information**\n\n"
                f"**Name:** {country_name}\n"
                f"**Capital:** {capital}\n"
                f"**Region:** {region} — {subregion}\n"
                f"**Population:** {population:,}\n"
                f"**Area:** {area:,} km²\n\n"
                f"_Powered by @SECRECT_BOT_UPDATES"
            )
        else:
            text = "» Country information could not be fetched."

    except requests.exceptions.HTTPError:
        text = "» Invalid country code. Use a valid ISO code like `IN`, `US`, `GB`."
    except Exception as err:
        print(f"[Population Error] {err}")
        text = "» An unexpected error occurred. Please try again later."

    await message.reply_text(text, parse_mode=ParseMode.MARKDOWN)
