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
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app

TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

_TMDB_KEY = "23c3b139c6d59ebb608fe6d5b974d888"
_TMDB_BASE = "https://api.themoviedb.org/3"


async def TeamDev_get_movie_info(query: str) -> str:
    async with httpx.AsyncClient(timeout=10.0) as client:
        search = await client.get(
            f"{_TMDB_BASE}/search/movie", params={"api_key": _TMDB_KEY, "query": query}
        )
        results = search.json().get("results")
        if not results:
            return "» Movie not found."

        movie_id = results[0]["id"]
        details_resp = await client.get(f"{_TMDB_BASE}/movie/{movie_id}", params={"api_key": _TMDB_KEY})
        d = details_resp.json()

        cast_resp = await client.get(f"{_TMDB_BASE}/movie/{movie_id}/credits", params={"api_key": _TMDB_KEY})
        actors = ", ".join(a["name"] for a in cast_resp.json().get("cast", [])[:5]) or "N/A"

        title = d.get("title", "N/A")
        release = d.get("release_date", "N/A")
        overview = d.get("overview", "N/A")
        rating = d.get("vote_average", "N/A")
        revenue = d.get("revenue", 0)
        revenue_str = f"${revenue:,}" if revenue else "Not Available"

        return (
            f"» **Title:** {title}\n"
            f"» **Release Date:** {release}\n"
            f"» **Rating:** {rating}/10\n"
            f"» **Top Cast:** {actors}\n"
            f"» **Box Office:** {revenue_str}\n\n"
            f"» **Overview:**\n{overview}\n\n"
            f"_Powered by @SECRECT_BOT_UPDATES"
        )


@app.on_message(filters.command("movie") & ~BANNED_USERS)
async def mr_d_movie_command(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "» Please provide a movie name.\n\nExample: `/movie Inception`",
            parse_mode=ParseMode.MARKDOWN,
        )

    movie_name = " ".join(message.command[1:])
    status = await message.reply_text("» Searching for the movie…")
    try:
        info = await TeamDev_get_movie_info(movie_name)
        await status.edit_text(info, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        print(f"[Movie Error] {e}")
        await status.edit_text("» Failed to fetch movie information.")
