""""
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

import random
import string

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BANNED_USERS
from TeamDevXMusic import app


TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

_CHARSET = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?"


def TeamDev_generate_password(length: int = 16) -> str:
    length = max(8, min(64, length))
    return "".join(random.choices(_CHARSET, k=length))


@app.on_message(filters.command(["genpassword", "genpw"]) & ~BANNED_USERS)
async def mr_d_genpassword(_, message: Message):
    length = 16
    if len(message.command) > 1:
        try:
            length = int(message.command[1])
        except ValueError:
            pass

    password = TeamDev_generate_password(length)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Regenerate", callback_data=f"genpw:{length}")]
    ])

    await message.reply_text(
        f"» **Generated Password ({length} chars):**\n\n`{password}`\n\n"
        f"⚠️ _Do not share this password with anyone._\n"
        f"Powered by @Team_X_Og",
        reply_markup=keyboard,
        quote=True,
    )


@app.on_callback_query(filters.regex(r"^genpw:(\d+)$"))
async def team_x_og_genpw_regen(_, query):
    length = int(query.data.split(":")[1])
    password = TeamDev_generate_password(length)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Regenerate", callback_data=f"genpw:{length}")]
    ])
    try:
        await query.message.edit_text(
            f"» **Generated Password ({length} chars):**\n\n`{password}`\n\n"
            f"⚠️ _Do not share this password with anyone._\n"
            f"_Powered by @Team_X_Og_",
            reply_markup=keyboard,
        )
    except Exception:
        pass
    await query.answer("New password generated!")
