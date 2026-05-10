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

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app

TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

@app.on_message(filters.command("encode") & ~BANNED_USERS)
async def TeamDev_encode(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "» Provide text to encode.\nExample: `/encode hello world`"
        )
    text = message.text.split(None, 1)[1]
    encoded = text.encode("utf-8").hex()
    await message.reply_text(
        f"» **Encoded (Hex):**\n`{encoded}`",
        quote=True,
    )


@app.on_message(filters.command("decode") & ~BANNED_USERS)
async def mr_d_decode(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "» Provide hex to decode.\nExample: `/decode 68656c6c6f`"
        )
    hex_str = message.text.split(None, 1)[1].strip()
    try:
        decoded = bytes.fromhex(hex_str).decode("utf-8")
        await message.reply_text(
            f"» **Decoded (Text):**\n`{decoded}`",
            quote=True,
        )
    except ValueError:
        await message.reply_text("» Invalid hex string. Please provide a valid hex.")
