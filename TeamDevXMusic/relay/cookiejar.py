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


import os
import aiohttp
import aiofiles
import asyncio

import config
from ..logcfg import LOGGER


async def fetch_content(session: aiohttp.ClientSession, url: str):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    except aiohttp.ClientError as e:
        LOGGER(__name__).error(f"Error fetching from {url}: {e}")
        return ""


async def save_file(content: str, file_path: str):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        async with aiofiles.open(file_path, "w") as file:
            await file.write(content)
        return file_path
    except Exception as e:
        LOGGER(__name__).error(f"Error saving file {file_path}: {e}")
        return ""


async def save_cookies():
    full_url: str = str(config.COOKIES)
    paste_id: str = full_url.split("/")[-1]
    pastebin_url: str = f"https://batbin.me/raw/{paste_id}"

    async with aiohttp.ClientSession() as session:
        content = await fetch_content(session, pastebin_url)

        if content:
            file_path = "cookies/cookies.txt"
            saved_path = await save_file(content, file_path)

            if saved_path and os.path.getsize(saved_path) > 0:
                LOGGER(__name__).info(f"Cookies saved successfully to {saved_path}.")
            else:
                LOGGER(__name__).error("Failed to save cookies or the file is empty.")
        else:
            LOGGER(__name__).error("Failed to fetch cookies.")
