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

import re

import httpx
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app

TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

_ANILIST_URL = "https://graphql.anilist.co"
_QUERY = """
query ($anime: String) {
  Media (search: $anime, type: ANIME) {
    id
    title { romaji english native }
    description(asHtml: false)
    episodes
    status
    averageScore
    coverImage { large }
  }
}
"""


async def TeamDev_fetch_anime(name: str):
    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.post(
            _ANILIST_URL, json={"query": _QUERY, "variables": {"anime": name}}
        )
    data = resp.json()
    if "errors" in data:
        return None, f"» Error: {data['errors'][0]['message']}"
    return data["data"]["Media"], None


def mr_d_clean_description(desc: str | None) -> str:
    if not desc:
        return "No description available."
    desc = re.sub(r"<br\s*/?>", "\n", desc)
    desc = re.sub(r"<[^>]+>", "", desc)
    return (desc.strip()[:800] + "…") if len(desc) > 800 else desc.strip()


@app.on_message(filters.command("anime") & ~BANNED_USERS)
async def team_x_og_anime_info(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "» Please provide an anime name.\n\nExample: `/anime Naruto`",
            parse_mode=ParseMode.MARKDOWN,
        )

    anime_name = " ".join(message.command[1:])
    result, error = await TeamDev_fetch_anime(anime_name)

    if not result:
        return await message.reply_text(error or "» Anime not found.")

    title = result["title"]["romaji"]
    english = result["title"].get("english")
    native = result["title"]["native"]
    episodes = result.get("episodes", "N/A")
    status = result.get("status", "N/A")
    score = result.get("averageScore", "N/A")
    desc = mr_d_clean_description(result.get("description"))
    image = result["coverImage"]["large"]

    eng_line = f"**» Title (English):** {english}\n" if english else ""
    caption = (
        f"**» Title (Romaji):** {title}\n"
        f"{eng_line}"
        f"**» Title (Native):** {native}\n"
        f"**» Episodes:** {episodes}\n"
        f"**» Score:** {score}/100\n"
        f"**» Status:** {status}\n\n"
        f"**» Description:**\n{desc}\n\n"
        f"_Powered by @SECRECT_BOT_UPDATES_"
    )

    await message.reply_photo(image, caption=caption, parse_mode=ParseMode.MARKDOWN)
