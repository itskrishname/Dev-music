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

import os

import aiofiles
import aiohttp
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app

TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

_RMBG_API_KEY = "23nfCEipDijgVv6SH14oktJe"


def TeamDev_unique_filename(base: str) -> str:
    if not os.path.exists(base):
        return base
    name, ext = os.path.splitext(base)
    count = 1
    while True:
        candidate = f"{name}_{count}{ext}"
        if not os.path.exists(candidate):
            return candidate
        count += 1


async def mr_d_remove_background(image_path: str) -> tuple:
    headers = {"X-API-Key": _RMBG_API_KEY}
    async with aiohttp.ClientSession() as session:
        try:
            with open(image_path, "rb") as img:
                data = {"image_file": img.read()}
            async with session.post(
                "https://api.remove.bg/v1.0/removebg",
                headers=headers,
                data=data,
            ) as response:
                if "image" not in response.headers.get("content-type", ""):
                    return False, await response.json()
                out_path = TeamDev_unique_filename("no_bg.png")
                async with aiofiles.open(out_path, "wb") as f:
                    await f.write(await response.read())
                return True, out_path
        except Exception as e:
            return False, {"title": "Unknown Error", "errors": [{"detail": str(e)}]}


@app.on_message(filters.command("rmbg") & ~BANNED_USERS)
async def team_x_og_rmbg_command(_, message: Message):
    status = await message.reply_text("» Processing your image…")
    replied = message.reply_to_message

    if not replied or not replied.photo:
        return await status.edit_text("» Please reply to a photo to remove its background.")

    try:
        downloaded = await _.download_media(replied)
        success, result = await mr_d_remove_background(downloaded)
        os.remove(downloaded)

        if not success:
            error = result.get("errors", [{}])[0]
            return await status.edit_text(
                f"» **ERROR:** {result.get('title', 'Unknown')}\n{error.get('detail', '')}"
            )

        await message.reply_photo(
            photo=result,
            caption="» Background removed!\n\nPowered by @Team_X_Og",
        )
        await message.reply_document(document=result)
        os.remove(result)
        await status.delete()

    except Exception as e:
        await status.edit_text(f"» Failed to process the image.\nError: `{e}`")
